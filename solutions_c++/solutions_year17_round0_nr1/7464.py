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
int t;
int k,len;
char pancake[10000];


int main()
{
	//srand (time(NULL));
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		int count = 0;
		scanf("%s",pancake);
		scanf("%d",&k);
		len = strlen(pancake);
		for(int i=0;i<len-k+1;i++)
		{
			if(pancake[i]=='-')
			{
				count++;
				for(int j=0;j<k;j++)
				{
					pancake[i+j] = pancake[i+j]=='-'? '+':'-';
				}
			}
		}
		bool isall_1 = true;
		for(int i=0;i<len;i++)
		{
			if(pancake[i]=='-')
			{
				isall_1 = false;
				break;
			}
		}
		if(isall_1) printf("Case #%d: %d\n",t,count);
		else printf("Case #%d: IMPOSSIBLE\n",t);
	}
	return 0;
}