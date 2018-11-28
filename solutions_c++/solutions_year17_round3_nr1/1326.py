#include <cstdio>
#include <cmath>
#include <algorithm>
#include <utility>
#include <vector>
using namespace std;

typedef pair<int, int> ii;

bool compare(const ii& a, const ii& b)
{
	return a.first * 1LL * a.second > b.first * 1LL * b.second;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		vector<ii> pancakes;
		for(int i = 0; i < N; i++)
		{
			int r, h;
			scanf("%d%d", &r, &h);
			pancakes.push_back(ii(r, h));
		}
		
		sort(pancakes.begin(), pancakes.end(), compare);
		
		double best = 0.0;
		for(int i = 0; i < N; i++)
		{
			double total = M_PI * pancakes[i].first * pancakes[i].first
							+ 2.0 * M_PI * pancakes[i].first * pancakes[i].second;
			
			int p = 0;
			for(int j = 0; j < K - 1; j++)
			{
				if(p == i) p++;
				total += 2.0 * M_PI * pancakes[p].first * pancakes[p].second;
				p++;
			}
			
			best = max(best, total);
		}
		
		printf("Case #%d: %.9f\n", t, best);
	}
}
