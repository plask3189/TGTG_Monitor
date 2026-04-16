# Monitoring status of tgtg bags
(Ideally)
This automates the purchasing of a tgtg bag. 

(Currently)
It monitors the availability of your favorited bags.

## Setup:
To set up mac as a proxy between tgtg servers and the app:
https://den.dev/blog/intercepting-iphone-traffic-mac-for-free/

Identify the POST command which looks like this:

![Post](post3.png)

The request contains keys authorization, x-correlation-id, and cookie values. Use these in the headers.yaml file. 

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
