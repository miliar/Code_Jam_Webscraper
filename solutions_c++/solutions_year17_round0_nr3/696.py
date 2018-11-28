#include <bits/stdc++.h>
using namespace std;

long long n, m;

void work() {
	map<long long, long long> dict;
	priority_queue<long long> pq;
	pq.push(n);
	long long last;
	long long cnt = 0;
	dict[n] = 1;
	while (cnt < m) {
		long long u = pq.top();
		last = u;
		pq.pop();
		cnt += dict[u];
		long long a = u / 2;
		long long b = (u - 1) / 2;
		if (dict[a] == 0 && a != 0) {
			pq.push(a);
		}
		dict[a] += dict[u];

		if (dict[b] == 0 && b != 0) {
			pq.push(b);
		}
		dict[b] += dict[u];
	}
	long long ans = last - 1;
	printf("%lld %lld\n", (ans + 1) / 2, ans / 2);
}

int main()
{
	int t;
	scanf("%d", &t);
	int case_num = 0;
	while (t--)
	{
		case_num++;
		printf("Case #%d: ", case_num);
		scanf("%lld%lld", &n, &m);
		work();
	}
	return 0;
}
