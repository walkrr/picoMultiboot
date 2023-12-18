
#include <stdio.h>
#include <stdlib.h>


// GBA multiboot includes
#include "gba/multiboot.h"
#include "gba_rom.hpp"



int main() {
	size_t romSize = sizeof(gbaArray)
	gba::sendGBARom(gbaArray, romSize);
	return 0;
}
