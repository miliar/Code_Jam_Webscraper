#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

#define DEBUG	0

#define INT64	unsigned long long

int T;
INT64 K, N;

void solve()
{
	while (K > 1)
	{
		if (K % 2 == 0)
			N = ceil((N - 1) / 2.);
		else
			N = floor((N - 1) / 2.);

		K = K / 2;
	}

	INT64 max = ceil((N - 1) / 2.);
	INT64 min = floor((N - 1) / 2.);

	cout << max << " " << min << endl;
}


int main()
{
	if (DEBUG) freopen("C-small-2-attempt0.in", "r", stdin);
	if (DEBUG) freopen("C-small-2-attempt0.out", "w", stdout);

	cin >> T;
	for (int t = 0; t < T; t++)
	{
		cin >> N >> K;

		cout << "Case #" << t + 1 << ": ";

		solve();

		cout << endl;
	}

	return 0;
}
