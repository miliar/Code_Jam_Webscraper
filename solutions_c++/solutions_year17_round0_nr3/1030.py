#include <cstdio>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

typedef long long llint;

int main()
{
	int T;
	llint N, K;
	llint maxi, mini;
	priority_queue<pair<llint, llint>> PQ;
	
	freopen("input_C.txt", "r", stdin);
	freopen("output_C.txt", "w", stdout);

	scanf("%d", &T);

	for(int test_case=1;test_case<=T;test_case++)
	{
		scanf("%lld %lld", &N, &K);

		while(!PQ.empty()) PQ.pop();

		PQ.push({N, 1});

		llint cnt = 0;

		while(cnt < K)
		{
			llint curNum, curCnt;

			curNum = PQ.top().first;
			curCnt = PQ.top().second;
			PQ.pop();

			while(!PQ.empty() && PQ.top().first == curNum)
			{
				curCnt += PQ.top().second;
				PQ.pop();
			}

			maxi = (curNum)/2;
			mini = (curNum-1)/2;

			PQ.push({maxi, curCnt});
			PQ.push({mini, curCnt});

			cnt += curCnt;
		}

		printf("Case #%d: %lld %lld\n", test_case, maxi, mini);
	}

	return 0;
}
