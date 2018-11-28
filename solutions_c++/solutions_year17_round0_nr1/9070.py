#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<cstdio>
#include<queue>
#include<vector>
#include<string.h>
#include<math.h>
#include<stack>
#include<queue>
#include<deque>
#include<list>
using namespace std;

char pan[1001];
int k;

int main() {
	
	FILE *inf;
	inf = fopen("output.txt", "w");
	
	int t,rst,flag;

	scanf("%d", &t);
	for (int test = 1; test <= t; test++) {
		rst = 0,flag=0;
		scanf("%s %d", pan, &k);
		int len = strlen(pan);
		for (int i = 0; i <= len - k; i++)
		{
			if (pan[i] == '-')
			{
				rst++;
				for (int j = i; j < i+k; j++)
				{
					if (pan[j] == '-')
						pan[j] = '+';
					else
						pan[j] = '-';
				}
			}
		}
		for (int i = 0; i < len; i++)
			if (pan[i] == '-')
				flag = 1;

		flag == 1 ? fprintf(inf,"Case #%d: IMPOSSIBLE\n", test) : fprintf(inf,"Case #%d: %d\n", test, rst);
	}



	fclose(inf);

}




