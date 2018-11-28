#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#define MAX_N 
using namespace std;
int n,p;
int gr[5];
void clear()
{
	for (int i = 0; i < 5; ++i)
		gr[i] = 0;
}
void solve()
{
	int res = gr[0];
	for (int i = 1; i < p; ++i)
	{
		if (i != p - i) {
			int m = min(gr[i], gr[p - i]);
			res += m;
			gr[i] -= m;
			gr[p - 1] -= m;
		}
		else
		{
			res += gr[i] / 2;
			gr[i] = gr[i]%2;
		}

	}
	if (p == 3)
	{
		res += gr[1] / 3 + gr[2] / 3;
		gr[1] = gr[1] % 3;
		gr[2] = gr[2] % 3;
	}
	if (p == 4) {
		res += gr[1] / 4 + gr[3] / 4;
		gr[1] = gr[1] % 4;
		gr[3] = gr[3] % 4;
	}
	if ( gr[1] || gr[2] || gr[3] || gr[4])res++;
	cout << res << "\n";
}
void input()
{
	cin >> n >> p;
	for (int i = 0; i < n; ++i)
	{
		int s;
		cin >> s;
		gr[(p - (s%p)) % p] ++;
	}
}
int main()
{
	int t, m, n;
	cin >> t;
	for (int k = 1; k <= t; ++k)
	{
		clear();
		input();
		printf("Case #%d: ", k);
		solve();
	}
}