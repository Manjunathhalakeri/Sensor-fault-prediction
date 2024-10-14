import os
import sys
from Sensor.exception import SensorException
from Sensor.logger import get_logger

logger = get_logger(__name__)

def test_exception():
    try:
        logger.info("Starting the test_exception function")
        a=1/0
    except Exception as e:
        raise SensorException(e, sys)


if __name__ == "__main__":
    try:
        ##logging.info("Starting the sensor fault prediction project")
        ##raise Exception("Testing custom exception")
        test_exception()
    except Exception as e:
        ##raise SensorException(e, sys)
        print(e)