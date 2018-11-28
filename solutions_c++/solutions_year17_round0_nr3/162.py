#include <bits/stdc++.h>

using namespace std;

const int maxn = 1000;

void print(long long range)
{
	cout << (range - 1) / 2 << ' ' << range / 2 - 1 << endl;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		long long N, K, R;
		printf("Case #%d: ", t);
		cin >> N >> K;
		++N;
		for (R = 0; K > (1LL << R); ++R)
			K -= (1LL << R);
		// cout << R << ' ' << K << endl;
		if (K <= N - ((N >> R) << R))
			print((N >> R) + 1);
		else
			print(N >> R);
	}
}
