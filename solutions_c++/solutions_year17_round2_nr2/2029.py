//============================================================================
// Name        : CodeJam_C.cpp
// Author      : Kristiyan Balabanov
// Version     :
// Copyright   : All mine!!!
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <map>

#define lld long long

using namespace std;

int main()
{
	FILE* f = fopen("out.txt", "w+");

	short cases, total;
	short colours[6]; // red, orange, yellow, green, blue, violet
	char alphabet[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};

	scanf("%hd", &cases);

	for(short c = 1; c <= cases; ++c)
	{
		scanf("%hd %hd %hd %hd %hd %hd %hd", &total, &colours[0], &colours[1], &colours[2], &colours[3], &colours[4], &colours[5]);
		if((colours[0] > total / 2) || (colours[2] > total / 2) || (colours[4] > total / 2))
		{
			fprintf(f, "Case #%hd: IMPOSSIBLE\n", c);
			printf("Case #%hd: IMPOSSIBLE\n", c);
			continue;
		}

		fprintf(f, "Case #%hd: ", c);
		printf("Case #%hd: ", c);
		short last = -1;
		short first;
		for(int i = 0; i < total-2; ++i)
		{
			short maxI = 0;
			if(last == 0)
				maxI++;
			for(int j = 0; j < 6; ++j)
				if(colours[j] && (j != last)) // at least 1 remaining
					maxI = (colours[maxI] < colours[j]) ? j : maxI;
			putchar(alphabet[maxI]);
			putc(alphabet[maxI], f);
			if(i == 0)
				first = maxI;
			colours[maxI]--;
			last = maxI;
			//printf("last: %d\n", last);
		}
		for(int j = 0; j < 6; ++j)
			if(colours[j] && (j == first)) // at least 1 remaining
			{
				putchar(alphabet[j]);
				putc(alphabet[j], f);
				colours[j]--;
			}
		for(int j = 0; j < 6; ++j)
			if(colours[j]) // at least 1 remaining
			{
				putchar(alphabet[j]);
				putc(alphabet[j], f);
			}

		putchar(10);
		putc(10, f);
	}

	return 0;
}
