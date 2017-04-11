#!/usr/bin/env python

import mlbgame
import datetime

year, month, day = str(datetime.datetime.now().strftime('%Y,%-m,%-d')).split(',')

scores = mlbgame.day(int(year), int(month), int(day), home="Cubs")

for score in scores:
    print score
