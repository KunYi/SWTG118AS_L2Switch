SWTG118AS Hacking
===

The repository for keeping my work data

To modify an unmanaged switch to have L2 management features.

First, I want to thank [libc0607](https://github.com/libc0607), [up-n-atom](https://github.com/up-n-atom), [FanFansfan](https://github.com/FanFansfan), and others for their contributions. Their research on Realtek RTL8372 firmware and hardware made the possibility of easy upgrades feasible.

The repository merely collects their contributions and adapts them to suit my usage environment.

### Only tested/verified on Fudan FM25Q16A

1. download [firmware_full.bin](./firmwares/firmware_full.bin) and write it into the flash

2. Read the UID of the flash first, then modify the parameters of `get_uid()` in [enc.py](./enc.py) and execute the script. You will get an **otp.bin** file for updating the OTP zone of the flash.

3. If you need to update the MAC or another default configuration, run [calcsum.py](./calcsum.py) to update the firmware and re-flash.

### Reset Button issues

A 3.3K or 2.2K Ohm resistor needs to be placed at the R236 position on the PCB to pull the pink line high. R236 is located near the SPI NOR Flash. This resistor (R236) is used for pull-high, while R237 is used for pull-down. In this case, we need to pull the line high to resolve an issue with Reset Button detection

![Modify Pull High](./pcb/Modify.jpg)
avoid reset button issues, need to pull-high

![PCB_TOP](./pcb/PCB_Front.jpg)
<p style="text-align: center;">Top of PCB</p>

![PCB_BOTTOM](./pcb/PCB_Back.jpg)
<p style="text-align: center;">Bottom of PCB</p>

### References

* [Some detail of RTL8372 firmware & Any progress on reverse engineering the UID algorithm?](https://github.com/up-n-atom/SWTG118AS/issues/4)

