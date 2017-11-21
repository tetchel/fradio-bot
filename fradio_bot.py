#!/usr/bin/env python3

import urllib
import urllib.parse
import urllib.request
import time

# This bot continuously sends broadcast requests to our Fradio server, such that it is always broadcasting.
# Right now, it just plays The Royal Scam over and over :)

TRACKS = [ 
    ('spotify:track:3sqNXrDvCy4nid6XbaA2Cg', 278800),
    ('spotify:track:4IBoDzxcRRRhQ6dozP28aQ', 213800),
    ('spotify:track:1K9B43e0PyilYctK0WgoO4', 256360),
    ('spotify:track:3Vrw3TH5qkTReMFHVfI3v8', 264000),
    ('spotify:track:1FLQYGTaDYzGjpP9c82Q1G', 241000),
    ('spotify:track:34C3UVHdq8Uay5EzUHvJqH', 245000),
    ('spotify:track:4r4VpAcwrKtvX4klQ9EHUs', 351000),
    ('spotify:track:0awgWi0pDZ2qzxQL75DJtz', 235800),
    ('spotify:track:2hYS79fHfVPgxb8PHFksHJ', 390960)
]

BROADCAST_URL = 'http://ec2-35-182-236-140.ca-central-1.compute.amazonaws.com/broadcast?spotifyusername=RoyalScamBot&trackid={}&t=0&len={}&playing=1'

while True:
    for track in TRACKS:
        trackid = track[0]
        length = track[1]

        # Encode special chars
        trackid = urllib.parse.quote(trackid)
        broadcast = BROADCAST_URL.format(trackid, length)
        print('GETTING: ' + broadcast)

        response = urllib.request.urlopen(broadcast, timeout=10)

        print('RESPONSE: ' + response.read().decode('utf8'))
        print('Delaying {} ms for song to play'.format(length))
        time.sleep(length/1000)
