#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

pair<int, int> f(int a) {
	pair<int, int> p;
	p.first = (a-1)/2;
	p.second = a - p.first - 1;
	return p;
}

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d", &t);
	for (int testcase = 1; testcase <= t; ++testcase)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		priority_queue<int> pq;
		pq.push(n);

		pair<int, int> ans;
		ans.first = n;
		ans.second = n;

		for (int i = 0; i < k; ++i)
		{
			int now = pq.top();
			pq.pop();
			pair<int,int> p = f(now);
			ans.first = min(ans.first, p.first);
			ans.second = min(ans.second, p.second);
			pq.push(p.first);
			pq.push(p.second);
		}

		printf("Case #%d: ", testcase);
		printf("%d %d\n", ans.second, ans.first);
	}
	return 0;
}