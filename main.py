from mq import MQ
import time
from prometheus_client import start_http_server, Gauge

# Create a metric to track time spent and requests made.
smoke_ppm = Gauge('smoke_ppm_percent', 'Percentage of smoke PPM ')
lgp_ppm = Gauge('lpg_ppm_percent', 'Percentage of LPG PPM ')
co_ppm = Gauge('co_ppm_percent', 'Percentage of CO PPM ')


def main(interval: int) -> None:
    mq = MQ()
    start_http_server(8000)
    while True:
        perc = mq.MQPercentage()

        smoke_ppm.set(perc["SMOKE"])
        lgp_ppm.set(perc["GAS_LPG"])
        co_ppm.set(perc["CO"])

        time.sleep(interval)

if __name__ == "__main__":
    main(30)