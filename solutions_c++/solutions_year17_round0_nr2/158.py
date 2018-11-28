#include <bits/stdc++.h>

using namespace std;

const int maxn = 1000;

bool check(long long N)
{
	for (long long i = 1; i <= N; i *= 10)
		if ((N / i) % 10 < (N / (i * 10)) % 10)
			return false;
	return true;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		long long N, ans;
		printf("Case #%d: ", t);
		cin >> N;
		if (check(N))
		{
			cout << N << endl;
			continue;
		}
		for (long long i = 1; i <= N; i *= 10)
		{
			long long Ni = N / (i * 10);
			while (N / (i * 10) == Ni)
				N -= i;
			if (check(N))
				break;
		}
		cout << N << endl;
	}
}
