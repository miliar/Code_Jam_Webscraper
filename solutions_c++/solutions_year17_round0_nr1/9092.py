/* ***********************************************
Author        :5lyTher1n
Created Time  :2017/4/8 23:01:31
File Name     :\Users\dell\Desktop\cccc\GCJ\As.cpp
************************************************ */

#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <time.h>
using namespace std;

long T,t;
long k;
char str[1010];
long num[1010];

int main()
{
	freopen("1.in","r", stdin);
	freopen("1.out","w",stdout);

	scanf("%ld", &T);

	for(long t = 1; t <= T; t ++)
	{
		printf("Case #%ld: ",t);
		
		long ans = 0;
		
		scanf("%s", str);
		scanf("%ld", &k);
		memset(num,0,sizeof(num));
		long len = strlen(str);
		long start = -1;
		for(long i = 0; i < len; i ++)
		{
			if(str[i] == '-')
			{
				num[i] = 0;
				if(start == -1)start = i;
			}
			else num[i] = 1;
		}
		if(start == -1){printf("0\n");continue;}
		long end = 0;
		for(long i = start; i < len; i ++)
		{
			if( !num[i] )
			{
				if(i + k - 1 >= len)
				{
					printf("IMPOSSIBLE\n");
					end = -1;
					break;
				}
				for(long j = i; j < i + k; j ++)num[j] = !num[j];
				end ++;
			}
		}

		if( end != -1)
			printf("%ld\n", end);
		}
		return 0;
	}

		
