import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://ehub-cluster.servicebus.windows.net/;SharedAccessKeyName=localroot;SharedAccessKey=mw2wCrEbmvFgbVV7jJQ5rNdswmTDPcNn5XvX61BgQvE=", eventhub_name="topic1")
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        for i in range(1,100):
            event_data_batch.add(EventData('First event '+str(i)))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())