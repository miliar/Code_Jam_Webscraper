#include <iostream>
#include<cstring>

using namespace std;

int errorchk(char *flipstate,int size);
int chkcake(char *flipstate, int size);
void fliping(char &state);
int flip(char *flipstate,int size,int k);

int main()
{
	int case_size;
	int size[100];
	int flipsize[100];

	char flipstate[100][100];
	
	do {
		cin >> case_size;
	} while (1 > case_size || case_size > 100);
	for (int i=0; i < case_size; i++)
	{
			scanf("%s %d", flipstate[i], &flipsize[i]);
			size[i] = strlen(flipstate[i]);

	}
	for (int i = 0; i < case_size; i++) {
		int times;
		times=flip(flipstate[i], size[i], flipsize[i]);
		if (chkcake(flipstate[i], size[i]))
			printf("Case #%d: %d\n", i + 1, times);
		else
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
	}

}
int errorchk(char *flipstate,int size)
{
	for (int i = 0; i < size; i++)
	{
		if (flipstate[i] == '+' || flipstate[i] == '-')
		{
			return 0;
		}
	}
	return 1;
}
void fliping(char &state)
{
	if (state == '+')
		state = '-';
	else if (state == '-')
		state = '+';

}
int flip(char *flipstate, int size,int k)
{
	int times=0;
	for (int i = 0; i < size-k+1 ; i++) {
		if (flipstate[i] == '-')
		{
			if (i + k > size)
				break;
			for(int l=0;l<k;l++)
				fliping(flipstate[i+l]);

			times++;
		}
	}
	return times;
}
int chkcake(char *flipstate, int size)
{
	for (int i = 0; i < size; i++)
	{
		if (flipstate[i] == '-')
			return 0;
	}
	return 1;
}