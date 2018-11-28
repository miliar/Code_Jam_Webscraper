int MAX_DIGITS = 19;//4;
/// 1000 = 10^3, Max Digits: 4 = 3 + 1
/// 10^18 Max Digits: 18 + 1 = 19

#include "stdio.h"
#include "stdlib.h"
#include "string.h"
char* Digits;

/*
	Sweep left to right, examining pairs...
		If second item in pair is less than first item in pair:
			decrement first item,
			set all following items to '9'
			Sweep right to left, examining pairs...
				If second item in pair is less than first item in pair:
					decrement first item,
					set second item to '9'

	Sweep left to right, examining pairs...
		If second item in pair is less than first item in pair:
			decrement first item
			Sweeping backward, examining pairs...
				If second item in pair is less than first item in pair:
					decrement first item
				Otherwise
					Set everything later to '9'
*/
inline void MakeTidy ()
{
	char* cptr = Digits;
	// Start at 1 in order to not test an extra pair which includes the null character (and will overwrite it with a '9', causing a segfault).
	for (unsigned char pos = 1; pos < MAX_DIGITS; pos++)
	{
		char first = *cptr;
		char second = *++cptr;
		// Making the assumption that the character set is ASCII or otherwise has digits 0-9 in increasing order.
		if (first > second)
		{
			do
			{
				second = --(*cptr--);
				if (cptr < Digits) break;
				first = *cptr;
			}
			while (first > second);
			pos = ++cptr - Digits;
			while (++pos < MAX_DIGITS)
				(*++cptr) = '9';
			return;
		};
	};
};
inline char* RunTrial ()
{
	// Pad the number with preceding zeroes.
	unsigned char len = strlen(Digits);
	unsigned char padding = MAX_DIGITS - len;
	memmove(Digits + padding,Digits,len);
	memset(Digits,'0',padding);

	MakeTidy();
	char* out = Digits;
	while (*out == '0') out++; // Offset past the unnecessary zeroes.
	if (!*out) out--; // Show a single zero if the entire number is just 0.
	return out;
};
int main ()
{
	Digits = malloc(sizeof(char) * (MAX_DIGITS + 1)); // + 1 for null char
	*(Digits + MAX_DIGITS) = '\0'; // Only need to set the null once.
	unsigned short trialcount;
	if (!scanf("%hu",&trialcount))
	{
		printf("Error reading trial count!\n");
		return -1;
	};
	for (unsigned short trial = 1; trial <= trialcount; trial++)
	{
		if (!scanf("%s\n",Digits))
		{
			printf("Error reading trial #%hu!\n",trial);
			return -2;
		};
		printf("Case #%hu: %s\n",trial,RunTrial());
	};
	free(Digits);
};
