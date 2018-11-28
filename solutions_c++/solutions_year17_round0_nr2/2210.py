#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

void adjacentSort(char *number, int numlen, int pos)
{
	if (pos < 0 || pos+1 == numlen)
		return;

	if (number[pos] > number[pos+1]) {
		number[pos]--;
		for (int i = pos+1; i < numlen; ++i)
			number[i] = '9';

		adjacentSort(number, numlen, pos-1);
	}
}



void getLastTidyNum(char *originNum, char *lastTidyNum)
{
	int numlen;
	char number[20];
	char *numStartPtr;

	strcpy(number, originNum);
	numlen = strlen(number);

	for (int i = 0; i < numlen-1; ++i) {
		adjacentSort(number, numlen, i);
	}

	numStartPtr = &number[0];
	while (*numStartPtr == '0')
		numStartPtr++;

	strcpy(lastTidyNum, numStartPtr);
}
int main()
{
	int tcase;
	char number[20];
	char lastTidyNum[20];

	scanf("%d", &tcase);

	for (int i = 1; i <= tcase; ++i) {
		scanf("%s", number);
		getLastTidyNum(number, lastTidyNum);
		printf("Case #%d: %s\n", i, lastTidyNum);
	}
}
