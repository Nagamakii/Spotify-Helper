import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

scope = 'user-top-read'

user = input("User to make playlist from: ")

SPOTIPY_CLIENT_ID = 'SPOTIPY_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'SPOTIPY_CLIENT_SECRET'

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager(scope=scope))

def get_info(user):
    sp.current_user_top_tracks(limit=35,offset=0,time_range='medium_term')
