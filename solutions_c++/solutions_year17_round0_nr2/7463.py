#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <string>
#include <time.h>

#define SQR(_x) ((_x)*(_x))
#define MAX(_a,_b) _a>_b? _a:_b
#define MIN(_a,_b) _a<_b? _a:_b
#define NL printf("\n")
#define LL long long
#define DB double
#define PB push_back
#define INF 1000000000

using namespace std;
int T;
char num[10000];
int len;


int main()
{
	//srand (time(NULL));
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int string_shift = 0;
		int starting_index = 0;
		bool nondecreasing = true;
		scanf("%s",num);
		len = strlen(num);
		for(int i=1;i<len;i++)
		{
			if(num[i] < num[i-1])
			{
				nondecreasing = false;
				num[i-1]--;
				starting_index = i-1;
				break;
			}
		}
		if(not nondecreasing)
		{
			for(int i=starting_index+1;i<len;i++)
			{
				num[i] = '9';
			}
			for(int i=starting_index;i>0;i--)
			{
				if(num[i]<num[i-1])
				{
					num[i] = '9';
					num[i-1]--;
				}
				else break;
			}
		}
		if(num[0] == '0') string_shift = 1;
		printf("Case #%d: %s\n",t,num+string_shift);
	}
	return 0;
}