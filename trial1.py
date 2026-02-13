
print('print first list')

import datetime as dt
import logging
import time
logging.info("logging first Strategy execution started")

strategy_name = "supertrend_ema_strategy"
logging.basicConfig(level=logging.INFO, filename=f"{strategy_name}.log",filemode='a',format="%(asctime)s - %(message)s")
logging.getLogger('ib_async').setLevel(logging.CRITICAL)
logging.info("logging second Strategy execution started")
while True:
    # if dt.datetime.now() > end_time:
    #     break
    ct = dt.datetime.now()
    logging.info(f"log time Current time: {ct}")
    print(f" print time Current time: {ct}")
    time.sleep(60)