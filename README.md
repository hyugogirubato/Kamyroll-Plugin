![Kamyroll_Plugin](/resources/Kamyroll_plugin.png)  

## Description
This is a plugin providing options to enhance the [Kamyroll-Python](https://github.com/hyugogirubato/Kamyroll-Python) script in order to increase the potential of the original script.
 
## Features
- Connexion avec son compte
- Country bypass
- Premium bypass
- Available for all platforms (macOS, Windows, Linux, etc.)

## Requirements
- [Python](https://www.python.org/downloads) 3+

### Installation
```bash
pip install -r requirements.txt
```

## Information
 - The script provides a secure proxy for using the country bypass.
 - The generated data is saved directly in the kamyroll.json file.
 - Using the program requires generating the kamyroll.json file with the main script.
 - If the execution of the script ends without error or message, the data has been saved.
 - The country argument is can be used with the bypass and your account.
 - The country argument defaults to your location (no proxy generated).

## List of available regions
| Code | Country |
| ------------ | ------------ | 
| at | Argentina |
| at | Austria |
| au | Australia |
| be | Belgium |
| bg | Bulgaria |
| br | Brazil |
| ca | Canada |
| ch | Switzerland |
| cl | Chile |
| co | Colombia |
| cz | Czech Republic |
| de | Germany |
| dk | Denmark |
| es | Spain |
| fi | Finland |
| fr | France |
| gb | United Kingdom (Great Britain) |
| gr | Greece |
| hk | Hong Kong |
| hr | Croatia |
| hu | Hungary |
| id | Indonesia |
| ie | Ireland |
| il | Israel |
| in | India |
| is | Iceland |
| it | Italy |
| jp | Japan |
| kr | Korea, Republic of |
| mx | Mexico |
| nl | Netherlands |
| no | Norway |
| nz | New Zealand |
| pl | Poland |
| ro | Romania |
| ru | Russian Federation |
| se | Sweden |
| sg | Singapore |
| sk | Slovakia |
| tr | Turkey |
| uk | United Kingdom |
| us | United States of America |


## Arguments

### Login with ID
```bash
kamyroll --login "MAIL:PASSWORD"
kamyroll -l "MAIL:PASSWORD"
```

### Premium bypass
```bash
kamyroll --bypass
kamyroll -b
```

### Country bypass
```bash
kamyroll --country "COUNTRY_CODE"
kamyroll -c "COUNTRY_CODE"
```

---
*This script was created by the __Nashi Team__.  
Find us on [discord](https://discord.com/invite/g6JzYbh) for more information on projects in development.*
