import rtsp

#add your rtsp url and type your username / password for the stream
with rtsp.Client(rtsp_server_uri = 'rtsp://admin:password@192.168.1.134:554/Streaming/Channels/401') as client:
    client.preview()

