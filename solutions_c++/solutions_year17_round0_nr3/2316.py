#include<iostream>

using namespace std;

void Solve(long long n, long long k, long long &min, long long &max)
{
	min = n;
	max = n;
	long long maxCnt = 1, cnt = 1;
	while (k > cnt)
	{
		k -= cnt;
		long long minCnt = cnt - maxCnt;
		cnt <<= 1;
		if (max & 1 == 1) maxCnt = (maxCnt << 1) + minCnt;
		min = (min - 1) / 2;
		max = max / 2;
	}
	if (k <= maxCnt)
	{
		min = (max - 1) / 2;
		max = max / 2;
	}
	else
	{
		max = min / 2;
		min = (min - 1) / 2;
	}
}

int main()
{
	int T;
	cin >> T;
	for (int c = 1; c <= T; c++)
	{
		long long n, k, min, max;
		cin >> n >> k;
		Solve(n, k, min, max);
		cout << "Case #" << c << ": " << max << " " << min << endl;
	}
	return 0;
}