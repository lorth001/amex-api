# Description
This is a small script I wrote for retrieving user transaction details from American Express (AMEX).

# Background
AMEX hasn't made their APIs public yet (shame) and it doesn't appear that anyone else has done the dirty work of reverse-engineering their private APIs.  It took a bit of work to figure out, so I wanted to make it available here in case anyone else needs access to the same data.  Of course this script can also be expanded on if you need access to other data (rewards, statements, etc.), but I only needed transactions at the time of creation.

# Configuration
You will of course need the username and password for the account you are trying to access.  

You'll also need an "account_token", which is a private value that AMEX uses internally.  This "account_token" seems to be unique and directly tied to each account--it never changes.  You can find it in the page source with these steps:

1. Login to AMEX website
2. Right-click the page and select "View Page Source" (or similar depending on your browser)
3. Search for "account_token"

