print((lambda n: n < 3 and (0, 9, 18)[n] or n > 11 and 999999998 or (n & 1 and "10" + (n - 4) * "9" or "19" + (n - 5) * "9") + "8")(int(__import__("sys").stdin.read())))