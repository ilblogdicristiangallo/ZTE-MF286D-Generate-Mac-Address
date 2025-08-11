# ZTE-MF286D-Generate-Mac-Address
Recover lost MAC on ZTE MF286D by editing mtd2.bin backup. Keep OUI D4:72:26, generate new last 3 bytes (e.g. A3:1E:9C). Use hex editor or script to replace old MAC in file. Write modified mtd2.bin back via mtd write. Reboot. Ensures valid unicast MAC and restores network function. Always backup first.

# Startup

python ztemac.py

# Generate partition mtd2.bin
With the generated MAC address, open mtd2.bin in a hex editor. Locate the first 12 hex characters (e.g. D47226A31E9C), even if not displayed as a visible MAC. Replace these 6 bytes with the new MAC value. Save the modified mtd2.bin file for restoration.

# Install Serial port
To restore mtd2.bin via serial: start the modem and stop U-Boot using Putty (115200, press Esc at boot). Set static IP:

setenv ipaddr 192.168.32.1

setenv serverip 192.168.32.20

saveenv

Run TFTP64 on PC (IP static 192.168.32.20, Gateway 192.168.32.1), place mtd2.bin in folder. Then:

tftp mtd2.bin

nand erase 0x120000 0x80000

nand write 0x84000000 0x120000 0x80000

reset

# Install with OpenWRT

To restore mtd2.bin via OpenWrt: upload the file to /tmp using WinSCP. Then log in via SSH and run:

mtd write /tmp/mtd2.bin /dev/mtd2

This writes the file to the NAND partition. Wait for completion, then reboot:

reboot

Ensure the file is valid and keep a backup of the original.

# Tutorial now:
https://www.ilblogdicristiangallo.com/2025/03/come-generare-mac-address-per-zte-mf286d-in-caso-di-perdita.html
