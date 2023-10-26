import asyncio
import websockets

async def handler(websocket):
	while True:
		try:
			data = await websocket.recv()
			print(data)
		except websockets.ConnectionClosedOK:
			break
			
async def main():
	async with websockets.serve(handler, "", 8881):
		await asyncio.Future()

asyncio.run(main())
