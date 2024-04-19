import streamlink

def view_who_is_live():
    # open the tct file or give error
    try:
        with open("streamers.txt", "r") as file:
            streamers = file.read().splitlines()
    except FileNotFoundError:
        print("Error: 'streamers.txt' file not found.")
        return
    except Exception as e:
        print(f"Error reading 'streamers.txt': {e}")
        return

    # Check the live status for each streamer
    for streamer in streamers:
        twitch_url = f"https://twitch.tv/{streamer}"
        try:
            streams = streamlink.streams(twitch_url)
            if streams:
                print(f"{streamer} :: live")
            else:
                print(f"{streamer} :: not live")
        except Exception as e:
            print(f"Error checking live status for {streamer}: {e}")
            print(f"{streamer} :: not live")

def watch_stream(streamer_name):
    # Format the Twitch URL with the provided streamer name
    twitch_url = f"https://twitch.tv/{streamer_name}"
    
    # Attempt to retrieve the best stream available
    try:
        streams = streamlink.streams(twitch_url)
        if 'best' in streams:
            stream_url = streams['best'].url
            print("Best available stream URL:", stream_url)
            
            # Create a new instance of the VLC player with the stream URL
            player = vlc.MediaPlayer(stream_url)
            player.play()

            # Wait for the user to stop watching
            input("Press Enter to stop watching...")
            player.stop()
        else:
            print("No available streams found.")
    except Exception as e:
        print(f"An error occurred: {e}")
