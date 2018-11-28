#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <numeric>
#include <cstring>

typedef long long i64d;

using namespace std;

int main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out" , "w" , stdout);
	int cas;
	scanf("%d" , &cas);
	for (int ca = 1; ca <= cas; ca ++)
	{
		printf("Case #%d: " , ca);
        int d , n;
        scanf("%d %d" , &d , &n);
        double t = 0;
        for (int i = 0; i < n; i ++)
        {
            int k , s;
            scanf("%d %d" , &k , &s);
            t = max(t , (double)(d - k) / s);
        }
        printf("%lf\n" , d / t);
    }
    return 0;
}