import asyncio
import socket

TARGET = "127.0.0.1"
PORTS = range(1, 5000)
TIMEOUT = 1

async def scan_port(port):
    try:
        conn = asyncio.open_connection(TARGET, port)
        reader, writer = await asyncio.wait_for(conn, timeout=TIMEOUT)
        print(f"[+] Puerto abierto: {port}")
        writer.close()
        await writer.wait_closed()
    except:
        pass

async def main():
    tasks = [scan_port(port) for port in PORTS]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
