import asyncio
import websockets
from pose_detector import PoseDetector

all_clients = []


async def send_message(client_socket, message: str):
    await client_socket.send(message)


async def new_client_connected(client_socket, path):
    print("New client connected!")
    all_clients.append(client_socket)

    while True:
        new_message = await client_socket.recv()
        print("Client sent:", new_message)
        await send_message(client_socket, new_message)


async def start_server():
    print('Server started')
    await websockets.serve(new_client_connected, 'localhost', 12345)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()
