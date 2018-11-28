#include <vector>
#include <stack>
#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>
#include <functional>
#include <set>
#include <cstring>
#include <queue>
#include <stdlib.h>
#include <time.h>
#include <complex>
#include <iterator>
#include <regex>
#include <fstream>
#define all(o) (o).begin(), (o).end()
#define mp(x, y) make_pair(x, y)
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define sz(x) ((int)(x).size())
#define xx first
#define yy second
#define pt pair <double, double>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
const int S = int(3e5) + 10;
const int INF = int(1e9) + 7;
const ll MOD = ll(1e9) + 7;
const double EPS = 1e-12;
const ll magic = ll(5e4);
const int N = 1000;


int T, n, p, a[110];




int main()
{
	freopen("/Users/user/Downloads/A-small-attempt2.in", "r", stdin);
	freopen("key.out", "w", stdout);
	cin >> T;
	for(int q = 1; q <= T; q++)
	{
		cin >> n >> p;
		for(int i = 0; i < n; i++)
			scanf("%d", a + i);
		int res = 0;
		if(p == 2)
		{
			for(int i = 0; i < n; i++)
				res += (a[i] & 1);
			if(res > 0)
				res = n - res/2;
			else
				res = n;
		}
		else if(p == 3)
		{
			int num1 = 0, num2 = 0;
			for(int i = 0; i < n; i++)
			{
				if(a[i] % 3 == 1)
					num1++;
				if(a[i] % 3 == 2)
					num2++;
			}
			if(num1 > num2)
				swap(num1, num2);
			if(num2 == 0)
				res = n;
			else
			{
				num2--;
				if(num1 > num2)
					swap(num1, num2);
				res = n - (num1 + (((num2 - num1)/3)*2 + (num2 - num1)%3));
			}
		}
		printf("Case #%d: %d\n", q, res);
	}
	
	return 0;
}
