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
	
		scanf("%s", str);
		long len = strlen(str);

		long pd = 1;
		long one = -1;
		long i,j;
		for(i = 0,j = 0; i < len - 1; i ++,j++)
		{
			num[j] = str[i] - 48;
			num[j+1] = str[i+1] - 48;
			if( str[i] > str[i+1] )
			{
				pd = 0;
				if(one = -1)one = i + 1;
				
			}
		}
		if( pd )
		{
			printf("%s\n", str);
			continue;
		}
		for(long j = one ; j < len; j ++)num[j] = 9;
		one --;
		num[one] --;
		for(long i = one; i > 0; i --)
		{
			
			if(num[i] < num[i-1])
			{
				num[i] = 9;
				num[i-1] --;
			}
		}
		if( num[0] )printf("%ld", num[0]); 
		for(long i = 1; i < len - 1; i ++)
			printf("%ld", num[i]);
		printf("%ld\n", num[len-1]);
	}
	return 0;
}
			


