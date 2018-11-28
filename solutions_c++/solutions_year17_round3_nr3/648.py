#include <cstdio>
#include <vector>
#include <tuple>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	int N, K;
	double U;
	priority_queue<pair<double, int>> PQ;

	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("output-C-small-1.txt", "w", stdout);

	scanf("%d", &T);
	
	for(int test_case=1;test_case<=T;test_case++)
	{
		scanf("%d %d", &N, &K);
		scanf("%lf", &U);

		while(!PQ.empty()) PQ.pop();

		double t;
		for(int i=0;i<N;i++)
		{
			scanf("%lf", &t);
			PQ.push({-t, 1});
		}

		int qSize = N;

		while(qSize>=2 && U>0)
		{
			auto p1 = PQ.top(); PQ.pop(); qSize--;
			auto p2 = PQ.top();

			p1.first *= -1;	p2.first *= -1;

			if(U >= (p2.first - p1.first)*p1.second)
			{
				U -= (p2.first - p1.first)*p1.second;

				PQ.pop();
				PQ.push({-p2.first, p1.second + p2.second});
			}
			else
			{
				p1.first += U/p1.second;
				U = 0;

				PQ.push({-p1.first, p1.second}); qSize++;
			}
		}

		if(U>0)
		{
			auto p1 = PQ.top(); PQ.pop(); qSize--;
			p1.first *= -1;
			p1.first += U/p1.second;
			U = 0;
			PQ.push({-p1.first, p1.second}); qSize++;
		}

		double ans = 1;
		while(!PQ.empty())
		{
			for(int i=0;i<PQ.top().second;i++)
				ans *= -PQ.top().first;
			PQ.pop();
		}

		printf("Case #%d: %.9lf\n", test_case, ans);
	}


	return 0;
}