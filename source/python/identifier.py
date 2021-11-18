#!/usr/bin/env python
"""
Script: Kamyroll-Pyhton
Plugin: Identifier
Version: v2021.11.16
"""

import argparse
import json
from datetime import datetime
import requests
from xdg import BaseDirectory

CONFIG_FILE = 'kamyroll.json'


def get_login_form(args_login):
    try:
        username = args_login.split(':')[0].strip()
        password = args_login.split(':')[1].strip()
        return username, password
    except Exception:
        print('ERROR: Invalid login form.')
        exit(1)


def get_config():
    config_path = BaseDirectory.load_first_config(CONFIG_FILE)
    if config_path:
        file = open(config_path, 'r')
        config = json.load(file)
        file.close()
        return config
    else:
        print('ERROR: Configuration file not found.')
        exit(1)


def get_user_key(json_r, key):
    if json_r.get('data').get('user').get(key):
        return json_r.get('data').get('user').get(key)
    else:
        return ''


def save_config(config):
    config_path = BaseDirectory.load_first_config(CONFIG_FILE)
    file = open(config_path, 'w', encoding='utf-8')
    file.write(json.dumps(config, indent=4, sort_keys=False, ensure_ascii=False))
    file.close()


def get_proxy_key(json_r, key):
    if json_r.get('data').get('proxy').get(key):
        return json_r.get('data').get('proxy').get(key)
    else:
        print('ERROR: Proxy initialization error.')
        exit(1)


def get_expires():
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day + 1
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second
    expires = datetime.strptime('{}-{}-{}T{}:{}:{}Z'.format(year, month, day, hour, minute, second), '%Y-%m-%dT%H:%M:%SZ')
    return expires.strftime('%Y-%m-%dT%H:%M:%SZ')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--login',    '-l',  type=str,             help='Login')
    parser.add_argument('--bypass',   '-b',  action='store_true',  help='Bypass')
    parser.add_argument('--country',  '-c',  type=str,             help='Country')
    args = parser.parse_args()

    if not args.login and not args.bypass:
        print('ERROR: Login with a mandatory session.')
        exit(1)

    params = {'platform': 'mobile', 'bypass': args.bypass}
    if args.country:
        params['country'] = args.country

    if args.login:
        (account, password) = get_login_form(args.login)
        params['account'] = account
        params['password'] = password

    r = requests.get('https://kamyroll.herokuapp.com/auth/v1/token', params=params)
    if r.status_code == 200:
        json_r = r.json()
        json_config = get_config()
        json_config.get('configuration').get('token')['refresh_token'] = json_r.get('data').get('refresh_token')
        json_config.get('configuration').get('token')['bucket'] = json_r.get('data').get('cms').get('bucket')
        json_config.get('configuration').get('token')['policy'] = json_r.get('data').get('cms').get('policy')
        json_config.get('configuration').get('token')['signature'] = json_r.get('data').get('cms').get('signature')
        json_config.get('configuration').get('token')['key_pair_id'] = json_r.get('data').get('cms').get('key_pair_id')
        json_config.get('configuration').get('token')['expires'] = get_expires()
        json_config.get('configuration').get('account')['account_id'] = get_user_key(json_r, 'account_id')
        json_config.get('configuration').get('account')['external_id'] = get_user_key(json_r, 'external_id')
        json_config.get('configuration').get('account')['email'] = get_user_key(json_r, 'email')
        json_config.get('configuration').get('account')['password'] = get_user_key(json_r, 'password')
        json_config.get('configuration').get('account')['username'] = get_user_key(json_r, 'username')
        if json_r.get('data').get('proxy') is None:
            json_config.get('preferences').get('proxy')['is_proxy'] = False
            json_config.get('preferences').get('proxy')['uuid'] = ''
            json_config.get('preferences').get('proxy')['agent_key'] = ''
            json_config.get('preferences').get('proxy')['host'] = ''
            json_config.get('preferences').get('proxy')['port'] = ''
        else:
            json_config.get('preferences').get('proxy')['is_proxy'] = True
            json_config.get('preferences').get('proxy')['uuid'] = get_proxy_key(json_r, 'uuid')
            json_config.get('preferences').get('proxy')['agent_key'] = get_proxy_key(json_r, 'agent_key')
            json_config.get('preferences').get('proxy')['host'] = get_proxy_key(json_r, 'host')
            json_config.get('preferences').get('proxy')['port'] = get_proxy_key(json_r, 'port')
        save_config(json_config)
        print('[debug] Session generation completed.')
        exit(0)
    else:
        print('ERROR: Impossible to connect.')
        exit(1)


if __name__ == '__main__':
    main()
