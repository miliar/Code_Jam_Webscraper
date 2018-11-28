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

int T, n;
char a[105];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t)
	{
		scanf("%s", a);
		n = strlen(a);
		for(int i = 1; i < n; i++)
			if(a[i-1] > a[i])
			{
				a[i-1]--;
				for(int j = i; j < n; j++)
					a[j] = '9';
				i--;
				while(i > 0)
				{
					if(a[i-1] > a[i])
					{
						a[i-1]--;
						a[i] = '9';
					}
					i--;
				}
				break;
			}
		printf("Case #%d: %s\n", t, a + (a[0] == '0'));
	}
	return 0;
}