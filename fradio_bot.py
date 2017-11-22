#!/usr/bin/env python3

import urllib
import urllib.parse
import urllib.request
import time
import logging
import sys
from robots import robots

# This bot continuously sends broadcast requests to our Fradio server, such that it is always broadcasting.
# Right now, it just plays The Royal Scam over and over :)
TRACKS_ROYAL_SCAM = [ 
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
USER_ROYAL_SCAM = 'RoyalScamBot'

robots = robots()

BROADCAST_URL = 'http://ec2-35-182-236-140.ca-central-1.compute.amazonaws.com/broadcast?spotifyusername={}&trackid={}&t=0&len={}&playing=1'

logging.basicConfig(level=logging.INFO, filename="fradio-bot.log", format='%(asctime)s %(message)s')

userid = USER_ROYAL_SCAM
tracks = TRACKS_ROYAL_SCAM

if len(sys.argv) == 2:
    robot = sys.argv[1]
    if robot in robots:
        userid = robots[robot][0]
        tracks = robots[robot][1]
    else:
        print('Error: Invalid robot name')
        exit()

while True:
    logging.info("Enter while")
    for track in tracks:
        trackid = track[0]
        length = track[1]

        # Encode special chars
        trackid = urllib.parse.quote(trackid)
        broadcast = BROADCAST_URL.format(userid, trackid, length)
        #print('GETTING: ' + broadcast)
        logging.info('GETTING ' + broadcast)

        response = urllib.request.urlopen(broadcast, timeout=10)

        logging.info('RESPONSE: ' + response.read().decode('utf8'))
        logging.info('Delaying {} ms for song to play'.format(length))
        time.sleep(length/1000)

loggging.info("Exit while")
