#!/usr/bin/env python
import os

template = '''<?xml version="1.0"?>
<svg width="{width}" height="105" viewBox="0 0 {width} 105" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <rect x="0" y="0" rx="5" ry="5" width="{width}" height="105" style="fill: #333333" />
    <text x="15" y="35" font-family="Courier, monospace" font-size="27" fill="#ffffff">Darby Robocode Battle {battlenum}</text>
    <text x="15" y="60" font-family="Courier, monospace" font-size="15" fill="#aaaaaa">Won by:</text>
    <text x="25" y="85" font-family="Courier, monospace" font-size="20" fill="#ffffff">{winner}</text>
</svg>
'''

with open('results-columns.txt', 'r') as f:
    leaderboardLines = str(f.read()).splitlines()

winner = '[error finding winner]'
for line in leaderboardLines:
    if line.startswith('1st:'):
        winner = line[5:line.index(' ', 5)]

width = max(440, 63 + int(len(winner) * 11.7))


print template.format(width=width, winner=winner, battlenum=os.environ['CIRCLE_BUILD_NUM'])
