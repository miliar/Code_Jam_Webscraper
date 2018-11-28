#include<stdio.h>
#include<string.h>

char s[2000];
int slen;

void flip(int i)
{
	if       (s[i] == '+') s[i] = '-';
	else if  (s[i] == '-') s[i] = '+';
}

//flip pancake from i to j exclusive
bool flip(int i, int j)
{
	if(i < 0 || j > slen) return 0;
	for(int k = i; k < j; k++)
	{
		flip(k);
	}
	return 1;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int _t = 1; _t <= t; _t++)
	{
		scanf("%s", s);
		slen = strlen(s);

		int flipsize;
		scanf("%d", &flipsize);
		
		int count = 0;
		bool ispossible = true;

		for(int i = 0; i < slen; i++)
		{
			if(s[i] == '-')
			{
				bool check = flip(i, i + flipsize);
				if(check) count++;
				else ispossible = false;
			}
		}

		printf("Case #%d: ", _t);
		if(!ispossible) printf("IMPOSSIBLE");
		else            printf("%d", count);
		printf("\n");
	}
}





