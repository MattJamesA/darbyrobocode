#!/usr/bin/env python
import os

template = '''<?xml version="1.0"?>
<svg width="{width}" height="130" viewBox="0 0 {width} 130" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <rect x="0" y="0" rx="5" ry="5" width="{width}" height="130" style="fill: #333333" />
    <text x="15" y="35" font-family="Courier, monospace" font-size="27" fill="#ffffff">Darby Robocode Battle {battlenum}</text>
    <text x="15" y="60" font-family="Courier, monospace" font-size="15" fill="#aaaaaa">Won by:</text>
    <text x="25" y="85" font-family="Courier, monospace" font-size="20" fill="#ffffff">{winner}</text>
    <a xlink:href="https://darbycomputerclub.github.io/darbyrobocode/results-columns.txt">
        <text x="15" y="110" font-family="Courier, monospace" font-size="15" fill="#cccccc">see leaderboard</text>
    </a>
    <text x="165" y="110" font-family="Courier, monospace" font-size="15" fill="#aaaaaa">|</text>
    <a xlink:href="https://darbycomputerclub.github.io/darbyrobocode/darbybattle.br">
        <text x="187" y="110" font-family="Courier, monospace" font-size="15" fill="#cccccc">download record</text>
    </a>
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
