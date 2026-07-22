import os
os.system(" qemu-system-aarch64 -M virt -cpu cortex-a53 -nographic -kernel ./image.elf")
