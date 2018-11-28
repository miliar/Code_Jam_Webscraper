#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
using namespace std;
#define MAX_LENGTH 19

int main()
{
	int t, i, l, ptr;
	char s[MAX_LENGTH+1];
	scanf("%d\n", &t);
	for(i=1;i<=t;i++)
	{
		scanf("%s\n", s);
		l = strlen(s);
		ptr = 0;
		for(int j = 1; j < l; j++)
			if(s[j-1] > s[j])
			{
				ptr = j;
				for(int k = ptr; k < l; k++)
					s[k] = '9';
				s[ptr-1] = s[ptr-1] - 1;
				ptr--;
			}
		while(true)
		{
			if(ptr<=0)
				break;
			if(s[ptr-1] > s[ptr])
			{
				s[ptr] = '9';
				s[ptr-1] = s[ptr-1] - 1;
			}
			ptr--;
		}
		printf("Case #%d: ", i);
		for(ptr=0; ptr < l; ptr++)
			if(s[ptr] != '0')
				break;
		printf("%s", s+ptr);
		printf("\n");
	}

	return 0;
}
