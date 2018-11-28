//============================================================================
// Name        : CodeJam_Tidy_Numbers.cpp
// Author      : Kristiyan Balabanov
// Version     :
// Copyright   : All mine!!!
// Description :
//============================================================================

#include <stdio.h>

#define MAX_DIGITS 19 // 1E18

using namespace std;

short number[MAX_DIGITS];

int main()
{
	char c;
	short cases, digits, d;
	FILE* f = fopen("out.txt", "w+");

	scanf(" %hd ", &cases);

	for(short i = 1; i <= cases; ++i)
	{
		digits = 0;
		while((c = getchar()) != 10 && c != EOF)
		{
			number[digits] = c - '0';
			digits++;
		}

		for(d = digits-1; d > 0; --d)
		{
			if(number[d] < number[d-1])
			{
				number[d-1]--;
				for(short j = d; j < digits; ++j) // make all remaining digits 9s
					number[j]= 9;
			}
		}

		d = 0;
		while(!number[d]) d++; //skip leading 0s

		//printf("Case #%hd: ", i);
		fprintf(f, "Case #%hd: ", i);
		for(; d < digits; ++d)
			//printf("%hd", number[d]);
			fprintf(f, "%hd", number[d]);
		//putchar(10);
		putc(10,f);
	}

	return 0;
}
