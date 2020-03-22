import sys
import os
import spotipy
import spotipy.util as util

scope = 'ugc-image-upload,user-modify-playback-state,user-read-playback-state,user-read-currently-playing,user-top-read,user-read-playback-position,user-read-recently-played,	user-library-modify,user-library-read,user-follow-modify,user-follow-read,playlist-read-private,playlist-modify-public,playlist-modify-private,playlist-read-collaborative,user-read-private,user-read-email,app-remote-control,streaming'

username = 'eduardonamba'

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    volume = 8
    play = sp.volume(volume,device_id='73cb47ef5a6e6c42413e61f7b52bc0b2c0ab4167')
else:
    print("Can't get token for", username)
