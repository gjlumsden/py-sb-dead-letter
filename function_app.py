import time
import azure.functions as func
import logging
import random

app = func.FunctionApp()

@app.service_bus_queue_trigger(arg_name="azservicebus", queue_name="mysbqueue",
                               connection="servicebus_connection") 
def servicebus_queue_trigger(azservicebus: func.ServiceBusMessage):
    logging.info('Python ServiceBus Queue trigger processed a message: %s',
                azservicebus.get_body().decode('utf-8'))
    # log the delivery count
    logging.info('Delivery count: %s', azservicebus.delivery_count)
    # raise an error
    
    # Get the modulus of a random number
    random_number = random.randint(0, 100)
    # if the random number is even, raise an exception
    if random_number % 2 == 0:
        raise Exception("A failure has happened")
    else:
        logging.info("No exception raised")
    
    # sleep for 10 seconds
    time.sleep(10)