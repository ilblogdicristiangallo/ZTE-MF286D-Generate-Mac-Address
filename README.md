# ZTE-MF286D-Generate-Mac-Address
Recover lost MAC on ZTE MF286D by editing mtd2.bin backup. Keep OUI D4:72:26, generate new last 3 bytes (e.g. A3:1E:9C). Use hex editor or script to replace old MAC in file. Write modified mtd2.bin back via mtd write. Reboot. Ensures valid unicast MAC and restores network function. Always backup first.
