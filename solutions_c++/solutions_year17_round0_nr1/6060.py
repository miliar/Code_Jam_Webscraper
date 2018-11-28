#include "stdlib.h"
#include "stdio.h"
#include "string.h"
#define MAX_PANCAKES 1000
int main ()
{
	char* Pancakes = malloc(sizeof(char) * (MAX_PANCAKES + 1));
	unsigned short trialcount;
	if (!scanf("%hu",&trialcount))
	{
		printf("Error reading trial count!\n");
		return -1;
	};
	for (unsigned short trial = 1; trial <= trialcount; trial++)
	{
		unsigned short FlipperSize;
		if (scanf("%s %hu\n",Pancakes,&FlipperSize) < 2)
		{
			printf("Error reading trial #%hu!\n",trial);
			return -2;
		};
		unsigned short PancakeCount = strlen(Pancakes);
		unsigned short pos;
		char* PancakePtr = Pancakes;
		for (pos = 0; pos < PancakeCount; pos++, PancakePtr++)
			*PancakePtr = *PancakePtr == '+' ? 0 : 1;
		PancakePtr = Pancakes;
		PancakeCount -= FlipperSize;
		unsigned short FlipCount = 0;
		for (pos = 0; pos <= PancakeCount; pos++, PancakePtr++)
		{
			if (*PancakePtr)
			{
				FlipCount++;
				for (unsigned short i = 0; i < FlipperSize; i++, PancakePtr++)
					*PancakePtr = !*PancakePtr;
				PancakePtr -= FlipperSize;
			};
		};
		printf("Case #%hu: ",trial);
		for (pos = 1; pos < FlipperSize; pos++, PancakePtr++)
			if (*PancakePtr) goto FAILURE;
		printf("%hu\n",FlipCount);
		continue;
		FAILURE:
		if (*PancakePtr) printf("IMPOSSIBLE\n");
	};
	free(Pancakes);
};
