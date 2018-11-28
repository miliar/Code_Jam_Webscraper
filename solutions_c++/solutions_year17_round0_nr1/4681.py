//============================================================================
// Name        : CodeJam_Oversized_Pancake_Flipper.cpp
// Author      : Kristiyan Balabanov
// Version     :
// Copyright   : All mine!!!
// Description :
//============================================================================

#include <stdio.h>
#include <vector>

#define MAX_SIZE 1000
#define ALPHABET 2 // 0 or 1

using namespace std;

int main()
{
	char c;
	bool hasDashes;
	short cases, size, moves, firstDash, flipper;

	vector <bool> str(MAX_SIZE);
	FILE* f = fopen("out.txt", "w+");

	scanf(" %hd ", &cases);

	for(short caseI = 1; caseI <= cases; ++caseI)
	{
		size = 0;
		moves = 0;
		hasDashes = false;
		while((c = getchar()) != 32)
		{
			str[size] = !(c - 43); // '+' - 43 = 0, '-' - 43 = 2
			if(!hasDashes && c == 45) // first dash pos yet to be found
			{
				firstDash = size;
				hasDashes = true;
			}
			size++;
		}
		scanf(" %hd ", &flipper);

		if(!hasDashes)
		{
			fprintf(f, "Case #%hd: 0\n", caseI);
			//printf("Case #%hd: 0\n", caseI);
			continue;
		}

		short i = firstDash;
		while(i <= size - flipper)
		{
			//printf("i = %hd\n", i);
			if(str[i])
			{
				i++;
				continue;
			}
			moves++;
			hasDashes = false;
			for(int j = i; j < i + flipper; ++j)
			{
				if(!hasDashes && str[j] && (j != i))
				{
					hasDashes = true;
					firstDash = j;
				}
				str[j] = !str[j];
				/*for(int k = 0; k < size; ++k)
					printf("%c", str[k] + '0');
				printf("\n");*/
			}
			if(!hasDashes)
				i += flipper;
			else
				i = firstDash;
		}
		while(i < size)
		{
			if(!str[i])
			{
				hasDashes = true;
				break;
			}
			i++;
		}

		if(hasDashes)
			fprintf(f, "Case #%hd: IMPOSSIBLE\n", caseI);
			//printf("Case #%hd: IMPOSSIBLE\n", caseI);
		else
			fprintf(f, "Case #%hd: %hd\n", caseI, moves);
			//printf("Case #%hd: %hd\n", caseI, moves);
	}

	return 0;
}
