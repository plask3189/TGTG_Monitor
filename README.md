# Monitoring status of tgtg bags
(Ideally)
This automates the purchasing of a tgtg bag. 

(Currently)
It monitors the availability of your favorited bags.

## Setup:
To set up mac as a proxy between tgtg servers and the iphone app:

### Set up the toolchain mitmproxy

```bash
docker pull mitmproxy/mitmproxy
docker images
```

### Running mitmproxy
```bash
docker run --rm -it -v ~/.mitmproxy:/home/mitmproxy/.mitmproxy -p 8080:8080 mitmproxy/mitmproxy
```

### Capturing HTTP/S traffic
Get the IP address
```bash
ipconfig getifaddr en0
```

### Now in iPhone
Now you can set this up as a proxy on iPhone. Go to Settings > Wi-Fi > Currently Connected Network > Configure Proxy > Manual and enter the server IP and port (8080). Click save. While mitmproxy is running in terminal, go to mitm.it in Safari on iPhone and download the profile for iOS. 

Then go to the TGTG app.

Identify the POST command which looks like this:

![Post](post3.png)

The request contains keys `authorization`, `x-correlation-id`, and `cookie` values. Use these in the headers.yaml file. 

The response contains the item info and inventory.

## Run:
```bash
python check_fav_status.py
```

## Example Update:

```bash
Requested data at 2026-04-15 14:14:28.031640
Status: 200
+------------------------------------------------------------+---------------+----------------------------+
| Name                                                       | Available Qty |        Sold Out At         |
+------------------------------------------------------------+---------------+----------------------------+
|  Whole Foods - OH  - Cincinnati (Seafood Bag)              |       0       | 2026-04-14 10:15:46 PM EDT |
|  Whole Foods - OH  - Cincinnati (Dry Grocery Bag)          |       0       | 2026-04-14 10:16:31 PM EDT |
|  Whole Foods - OH  - Cincinnati (Frozen Grocery Bag)       |       0       | 2026-04-15 11:59:50 AM EDT |
|  Whole Foods - OH  - Cincinnati (Meat Bag)                 |       0       |            N/A             |
|  Whole Foods - OH  - Cincinnati (Specialty Foods Bag)      |       0       | 2026-04-14 10:01:33 PM EDT |
|  Whole Foods - OH  - Cincinnati (Prepared Foods Bag)       |       0       | 2026-04-14 10:16:28 PM EDT |
|  Whole Foods - OH  - Cincinnati (Refrigerated Grocery Bag) |       0       | 2026-04-14 10:17:32 PM EDT |
|  Whole Foods - OH  - Cincinnati (Bakery Bag)               |       0       | 2026-04-14 10:18:44 PM EDT |
|  Whole Foods - OH - Kenwood (Specialty Foods Bag)          |       0       |            N/A             |
|  Whole Foods - OH - Kenwood (Prepared Foods Bag)           |       0       | 2026-04-14 09:19:38 PM EDT |
|  Whole Foods - OH - Kenwood (Bakery Bag)                   |       0       | 2026-04-14 09:16:35 PM EDT |
+------------------------------------------------------------+---------------+----------------------------+
```


### References 
https://den.dev/blog/intercepting-iphone-traffic-mac-for-free/