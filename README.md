# Description
This is a small script I wrote for retrieving user transaction details from American Express (AMEX).

# Background
AMEX hasn't made their APIs public yet (shame) and it doesn't appear that anyone has done the dirty work of reverse-engineering their private APIs.  It took a bit of work to figure out, so I wanted to make it available for public consumption.  This script can be expanded if you need access to other data (rewards, statements, etc.).  I only needed transaction data at the moment, so that's all I've included.

# Configuration
All of the request info (headers, endpoints, and query) is configured in the "configs.yml" file.  The USERNAME, PASSWORD, and TOKEN fields from the config file are replaced with variables in the script, as well as the "start_date" and "end_date" query values.  Feel free to adjust as needed.

The TOKEN field (passed as "account_token" in the request headers) refers to a private value that AMEX uses internally.  This is a unique value associated with each account--it never changes.  You can find it in the page source with these steps:

1. Login to AMEX website
2. Right-click the page and select "View Page Source" (or similar depending on your browser)
3. Search for "account_token"

