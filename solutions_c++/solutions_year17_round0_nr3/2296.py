#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#include <algorithm>
#include <map>
using namespace std;

vector<long long> solution(long long N, long long K)
{
	priority_queue<pair<long long, long long> > pq;
	vector<long long> ans{ 0, 0 };
	long long p = 0;
	pq.push(make_pair(N, 1));
	while (true)
	{
		map<long long, long long> hash;
		while (!pq.empty())
		{
			pair<long long, long long> top = pq.top();
			pq.pop();
			ans[0] = (top.first - 1) / 2;
			ans[1] = top.first / 2;
			if (p + top.second >= K)			
				return ans;
			hash[ans[0]] += top.second;
			hash[ans[1]] += top.second;
			p += top.second;
		}
		for (auto x : hash)
			pq.push(make_pair(x.first, x.second));
	}
	return ans;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("google_C_large.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		long long N, K;
		scanf("%lld %lld", &N, &K);
		vector<long long> ans = solution(N, K);
		printf("Case #%d: %lld %lld\n", t, max(ans[0], ans[1]), min(ans[0], ans[1]));
	}
}
