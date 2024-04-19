import streamlink

streams = streamlink.streams("https://twitch.tv/xqc")
if 'best' in streams:
    stream_url = streams['best'].url
    print("Best available stream URL:", stream_url)
    
else:
    print("No available streams found.")
s