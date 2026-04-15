# every n minutes, submit the post request and check availability
import requests
import json
import time
from datetime import datetime
from zoneinfo import ZoneInfo
from prettytable import PrettyTable
import yaml
import subprocess

def get_status_of_favorites(headers):
    print(f"Requested data at {datetime.now()}")
    url = "https://api.toogoodtogo.com/api/item/v9/favorites"                
    payload = {                                                  
        "origin": {
            "latitude": 39.16246757887463,                       
            "longitude": -84.41944929357891
        },
        "paging": {
            "size": 50,
            "page": 0
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()                                  
    with open("fav_response.json", "w") as f:
        json.dump(response.json(), f, indent=2)
    print(f"Status: {response.status_code}")
    try:
        response.raise_for_status()
    except requests.HTTPError:
        print(
            "Request failed. If you got a 401, the JWT token likely expired and you need a fresh one.\n"
            "The DataDome cookie may also have expired or been invalidated."
        )
        return None
    data = response.json()
    return data  

def check_availability(data):
    table = PrettyTable()
    table.field_names = ["Name", "Available Qty", "Sold Out At"]
    table.align["Name"] = "l"

    for fav_item in data["favourite_items"]:
        name = fav_item["display_name"]
        available_quantity = fav_item["items_available"]
        when_soldout = fav_item.get("sold_out_at")

        if when_soldout is not None:
            dt_utc = datetime.fromisoformat(when_soldout.replace("Z", "+00:00"))
            dt_eastern = dt_utc.astimezone(ZoneInfo("America/New_York"))
            sold_out_str = dt_eastern.strftime("%Y-%m-%d %I:%M:%S %p %Z")
        else:
            sold_out_str = "N/A"

        flag = "✅" if available_quantity > 0 else ""
        table.add_row([f"{flag} {name}", available_quantity, sold_out_str])

    print(table)
    print("\n")
    available = [f for f in data["favourite_items"] if f["items_available"] > 0]
    if available:
        print()
        for f in available:
            print(f"  ⚡ Reserve {f['display_name']} soon! ({f['items_available']} left)")          
            msg = f"⚡ {f['display_name']} — {f['items_available']} left!"
            subprocess.run(["osascript", "-e", f'display notification "{msg}" with title "Too Good To Go" sound name "Default"'])   
if __name__ == "__main__":
    with open("headers.yaml") as f:
        headers= yaml.safe_load(f)
    while True:
        data = get_status_of_favorites(headers)
        check_availability(data )
        time.sleep(120)  # seconds
    
