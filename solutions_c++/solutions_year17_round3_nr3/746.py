#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <functional>

using namespace std;

double Solve(int N, int U, vector<int>& Ps)
{
	if (N == 1)
	{
		return (double)(Ps[0] + U) / 10000;
	}
	
	sort(Ps.begin(), Ps.end(), greater<int>());
	for (int i = N - 2; i >= 0 && U > 0; --i)
	{
		while (Ps[i] > Ps[i + 1] && U > 0)
		{
			for (int j = i + 1; j < N && U > 0; ++j)
			{
				++Ps[j];
				--U;
			}
		}
	}

	while (U > 0)
	{
		for (int i = 0; i < N && U > 0; ++i)
		{
			++Ps[i];
			--U;
		}
	}
	
	double ans = 1;
	for (int i = 0; i < N; ++i)
	{
		ans *= (double)Ps[i] / 10000;
	}
	
	return ans;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		int N, K;
		scanf("%d %d", &N, &K);
		int U1, U2;
		scanf("%d.%d", &U1, &U2);
		int U = U1 * 10000 + U2;

		vector<int> Ps;
		for (int j = 0; j < N; ++j)
		{
			int P1, P2;
			scanf("%d.%d", &P1, &P2);
			Ps.push_back(P1 * 10000 + P2);
		}
		
		printf("Case #%d: %.7f\n", i, Solve(N, U, Ps));
	}
	
	return 0;
}
