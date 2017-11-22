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

TRACKS_GROOVY = [
    ('spotify:track:1egLXYlUsAtNCSHHqYRtZJ',       59480),
    ('spotify:track:5hG8gvQ2d80Qoly4vfGOkH',      277546),
    ('spotify:track:4UoKkZIx4l2cMUoLUy5l5S',      338000),
    ('spotify:track:4oi05TamLuDSOhJRqoto7M',      631000),
    ('spotify:track:3XxpR8oXqq5Km5X4LlS0pi',      169003),
    ('spotify:track:3koCCeSaVUyrRo3N2gHrd8',      339320),
    ('spotify:track:6EVKzzNM0ZhEvJTBk2SACX',      253973),
    ('spotify:track:79KRVNCKAY5BLyFL4f0kFB',      564000),
    ('spotify:track:79KRVNCKAY5BLyFL4f0kFB',      564000),
    ('spotify:track:6NzOdf2JKluJVXEKjGDAMA',      509520),
    ('spotify:track:1ko2lVN0vKGUl9zrU0qSlT',      237000),
    ('spotify:track:6xQZuh6E5I7Ga9RNTXUM9k',      301000),
    ('spotify:track:583YTL8Fl6pCWtZAi2GvVZ',      221000),
    ('spotify:track:1GVGR00kvq0MlHHzIheNuJ',      343760),
    ('spotify:track:4MIXgItmCtVLCnT4BvU5tU',      262693),
]
USER_GROOVY = 'GrooveRobot'



def robots():
    return {  
        'royalscam':[USER_ROYAL_SCAM, TRACKS_ROYAL_SCAM],
        'groovy':[USER_GROOVY, TRACKS_GROOVY]
    }

