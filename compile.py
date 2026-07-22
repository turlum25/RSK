import os
x = "Y" 
y = "N"
os.system("rm image.elf")
os.system("aarch64-none-elf-gcc -Wall -O2 -nostdlib -nostartfiles -I./include -T linker.ld boot/head.S stubs.c main.c -o image.elf")
a = input("Run? (Y/N) ") 
if a == x: os.system(" qemu-system-aarch64 -M virt -cpu cortex-a53 -nographic -kernel ./image.elf")
elif a == y: exit()