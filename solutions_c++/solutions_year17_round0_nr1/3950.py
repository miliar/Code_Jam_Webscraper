#pragma comment(linker, "/STACK:500000000") 
#include <functional>
#include <algorithm>
#include <iostream> 
#include <string.h> 
#include <stdlib.h>
#include <complex>
#include <sstream> 
#include <fstream>
#include <numeric>
#include <ctype.h> 
#include <stdio.h> 
#include <bitset>
#include <vector> 
#include <string> 
#include <math.h> 
#include <time.h> 
#include <queue> 
#include <stack> 
#include <list>
#include <map> 
#include <set> 
using namespace std;

#define pi acos(-1.0)
#define eps 1e-9
#define mod 1000000007

int T, n, k;
char a[1005];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t)
	{
		scanf("%s %d", a, &k);
		n = strlen(a);
		int res = 0;
		for(int i = 0; i <= n - k; ++i)
		{
			if(a[i] == '-')
			{
				res++;
				for(int j = i; j < i + k; ++j)
					a[j] = (a[j] == '-' ? '+' : '-');
			}
		}
		bool ok = true;
		for(int i = 0; i < n; ++i)
			if(a[i] == '-')
			{
				ok = false;
				break;
			}
		printf("Case #%d: ", t);
		if(ok)
			printf("%d\n", res);
		else
			puts("IMPOSSIBLE");
	}
	return 0;
}