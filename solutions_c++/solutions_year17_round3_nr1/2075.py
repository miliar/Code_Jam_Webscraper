#include <iostream>
#include <string>
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

int min(int a, int b, int c)
{
	if (a <= b && a <= c)
		return a;
	if (b <= c)
		return b;
	return c;
}

int max(int a, int b, int c)
{
	if (a >= b && a >= c)
		return a;
	if (b >= c)
		return b;
	return c;
}

int main()
{
	const double Pi = 3.14159265358979323846;
	int T;
	int N, K;
	long long int R[1002], H[1002], RH[1002][2];
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> N >> K;
		for (int i = 0; i < N; i++)
		{
			cin >> R[i] >> H[i];
			RH[i][0] = R[i];
			RH[i][1] = R[i] * H[i];
		}
		
		
		long long int ansmax = 0;
		long long int ans = 0;
		for (int k = N - 1; k >= K - 1; k--)
		{
			ans = 0;
			for (int i = 0; i < N; i++)
				for (int j = i + 1; j < N; j++)
					if (RH[i][0] > RH[j][0])
					{
						swap(RH[i][0], RH[j][0]);
						swap(RH[i][1], RH[j][1]);
					}
			long long int rmax = RH[k][0];
			ans += rmax*rmax + 2 * RH[k][1];
			for (int i = 0; i < k; i++)
				for (int j = i + 1; j < k; j++)
					if (RH[i][1] > RH[j][1])
					{
						swap(RH[i][0], RH[j][0]);
						swap(RH[i][1], RH[j][1]);
					}
			for (int i = k - 1; i >= k - K + 1 && i >= 0; i--)
				ans += 2 * RH[i][1];
			if (ansmax < ans)
				ansmax = ans;
		}
		
		printf("Case #%d: %.6f\n", t, (double)ansmax*Pi);
	}

	return 0;
}