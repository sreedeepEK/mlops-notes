import logging 

## logging settings

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt=':5%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Arthemetic app") #logger name 

def add(a,b):
    result = a + b
    logger.debug(f"Adding {a} and {b} to get {result}")
    return result 

def subtract(a,b):
    result = a - b
    logger.debug(f"Subtracting {a} and {b} to get {result}")
    return result 

added = add(2,3)
subtracted = subtract(4,2)

print(added)
print(subtracted)