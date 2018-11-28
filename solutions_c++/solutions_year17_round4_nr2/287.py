	//     . .. ... .... ..... be name khoda ..... .... ... .. .     \\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;

int n, c, m;
int a[N], b[N];

int check(int x)
{
	int tot = 0;
	int cost = 0;
	for(int i = 0; i < n; i++)
	{
		cost += max(0, a[i] - x);
		tot += x - a[i];
		if(tot < 0)
			return -1;
	}
	return cost;
}

int main()
{
	int _t = in();
	for(int _i = 1; _i <= _t; _i++)
	{
		printf("Case #%d: ", _i);
		cin >> n >> c >> m;
		fill(a, a + n, 0);
		fill(b, b + c, 0);
		int mxB = 0;
		while(m--)
		{
			a[in() - 1]++;
			mxB = max(mxB, ++b[in() - 1]);
		}
		int L = mxB - 1, R = N;
		while(R - L > 1)
		{
			int mid = (R + L)/2;
			if(check(mid) != -1)
				R = mid;
			else
				L = mid;
		}
		cout << R << " " << check(R) << endl;
	}
}
