import asyncio
from aiortc import RTCPeerConnection, RTCSessionDescription


async def create_offer():
    # Create a new RTCPeerConnection
    pc = RTCPeerConnection()

    pc.createDataChannel("dataSendChannel")
    # audio transceiver must be created first for google
    # (per https://stackoverflow.com/questions/70281052/yet-another-invalid-argument-error-on-nest-battery-cam-generatewebrtcstream-comm),
    # and recvonly (per google spec)
    pc.addTransceiver("audio", direction="recvonly")
    pc.addTransceiver("video")

    await pc.setLocalDescription(await pc.createOffer())
    print(pc.localDescription.sdp)

    # Remember to close the connection
    await pc.close()


# Run the asyncio event loop
asyncio.run(create_offer())
