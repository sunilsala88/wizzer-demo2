
print('print first list')

import datetime as dt
import logging
import time
logging.info("logging first Strategy execution started")

strategy_name = "supertrend_ema_strategy"
print(strategy_name,'started')
while True:
    # if dt.datetime.now() > end_time:
    #     break
    ct = dt.datetime.now()
    print(f" print time Current time: {ct}")
    time.sleep(60)