#!/usr/bin/env python3
import random, time, sys

cols = 25
rows = 12
chars = "0101101"
grid = [[" " for _ in range(cols)] for _ in range(rows)]

while True:
    grid.pop()
    new_row = [random.choice(chars) if random.random() > 0.8 else " " for _ in range(cols)]
    grid.insert(0, new_row)
    output = ""
    for row in grid:
        output += " ".join(row) + "\n"
    sys.stdout.write(output + "\n")
    sys.stdout.flush()
    time.sleep(0.1)
