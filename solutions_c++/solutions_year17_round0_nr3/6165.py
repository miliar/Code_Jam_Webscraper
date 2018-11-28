#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t=1; t<=T; t++)
	{
		priority_queue<int> pq;

		int N, K;
		cin >> N >> K;

		pq.push(N);
		for (int i = 0; i < K - 1; i++)
		{
			int x = pq.top();
			pq.pop();
			if (x % 2 != 0)
			{
				pq.push(x / 2);
				pq.push(x / 2);
			}
			if (x % 2 == 0)
			{
				pq.push(x / 2);
				pq.push(x / 2 - 1);
			}
		}

		int ans = pq.top();
		if (ans % 2 != 0)
		{
			printf("Case #%d: %d %d\n", t, ans / 2, ans / 2);
		}
		else
		{
			printf("Case #%d: %d %d\n", t, ans / 2, max(0, ans / 2 - 1));
		}
	}
}
