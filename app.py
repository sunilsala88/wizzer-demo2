
import logging
import time
from datetime import datetime
from zoneinfo import ZoneInfo

print('print first list')

logging.info("logging first Strategy execution started")
print('this line is written in wizzer')
strategy_name = "supertrend_ema_strategy"
print(strategy_name, 'started')

# Get current UTC time
dt_utc = datetime.now(ZoneInfo("UTC"))

# Convert to Indian Standard Time
dt_ist = dt_utc.astimezone(ZoneInfo("Asia/Kolkata"))

print("Indian Standard Time:", dt_ist)


while True:
    # if datetime.now() > end_time:
    #     break
    dt_utc = datetime.now(ZoneInfo("UTC"))
    ct = dt_utc.astimezone(ZoneInfo("Asia/Kolkata"))
    print(f" print time Current time: {ct}")
    time.sleep(60)