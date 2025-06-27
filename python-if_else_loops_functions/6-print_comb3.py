#!/usr/bin/env python3

for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print(f"{i:02d}{j:02d}")
        else:
            print(f"{i:02d}{j:02d}", end=", ")
