#include <stdint.h>

// Fix stuff in boot/head.S
uint64_t swapper_pg_dir[512] __attribute__((aligned(4096))) = {0};
uint64_t init_pg_dir[512] __attribute__((aligned(4096))) = {0};
uint64_t idmap_pg_dir[512] __attribute__((aligned(4096))) = {0};

void __init_el2_setup(void) {}
void __cpu_setup(void) {}
void __primary_switch(void) {}