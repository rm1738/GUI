import asyncio
from bleak import BleakClient


async def connect_and_send_data(address, uuid, data):
    async with BleakClient(address) as client:
        # Connect to the Bluetooth device
        await client.connect()

        # Write data to the Bluetooth device
        await client.write_gatt_char(uuid, bytearray(data))

        # Start receiving data from the Bluetooth device
        await client.start_notify(uuid, notification_handler)

        # Wait for a few seconds
        await asyncio.sleep(5)

        # Stop receiving data from the Bluetooth device
        await client.stop_notify(uuid)

        # Disconnect from the Bluetooth device
        await client.disconnect()


def notification_handler(sender, data):
    # Handle received data from the Bluetooth device
    print(f"Received data: {data}")


if __name__ == "__main__":
    address = ""  # Replace with the Bluetooth device address
    uuid = ""  # Replace with the UUID of the characteristic to write to and notify
    data = ['w']  # Replace with the data to send

