#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main()
{
	long long int T, S, N, K, D;
	double ans = INFINITY, mb = 0;

	cin >> T;
	for (long long int t = 1; t <= T; t++)
	{
		ans = INFINITY;
		cin >> D >> N;
		for (long long int i = 0; i < N; i++)
		{
			cin >> K >> S;
			mb = ((double)D / (D - K))*S;
			if (mb < ans)
				ans = mb;
		}
		printf("Case #%I64d: %.6f\n", t, ans);
	}
	return 0;
}