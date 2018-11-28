#include <bits/stdc++.h>
using namespace std;

int test, n, k;
double a[1111];

int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> test;
	for(int t = 1; t <= test; t++)
	{
		cin >> n >> k;
		double u;
		cin >> u;
		for(int i = 0; i < n; i++)
			cin >> a[i];
		while(u > 0.00005)
		{
			int x = 0;
			for(int i = 0; i < n; i++)
				if(a[i] < a[x]) x = i;
			if(a[x]+0.0001 < 1.00005) a[x] += 0.0001;
			u -= 0.0001;
		}
		double rs = 1.0;
		for(int i = 0; i < n; i++)
			rs *= a[i];
		printf("Case #%d: %0.7f\n", t, rs);
	}
	return 0;
}