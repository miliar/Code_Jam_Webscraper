#include<cstdio>
#include<queue>

using namespace std;

typedef pair<int, pair<int, int> > pp;

int main()
{
	freopen("in.in", "rt", stdin);
	freopen("out.out", "w", stdout);
	int test, n, k;

	scanf("%d", &test);

	for (int t = 0; t < test; t++)
	{
		scanf("%d%d", &n, &k);
		priority_queue<pp> pq;
		pq.push(make_pair(n, make_pair(0, n + 1)));
		pp cur;

		while (k--)
		{
			cur = pq.top();
			pq.pop();
			int ind = (cur.first+1) / 2 + cur.second.first;
			pq.push(make_pair(ind - cur.second.first - 1, make_pair(cur.second.first, ind)));
			pq.push(make_pair(cur.second.second - ind - 1, make_pair(ind, cur.second.second)));
		}

		int last = (cur.first+1) / 2 + cur.second.first;

		printf("Case #%d: %d %d\n", t+1, max(last - cur.second.first - 1, cur.second.second - last - 1), min(last - cur.second.first - 1, cur.second.second - last - 1));
	}

	return 0;
}
