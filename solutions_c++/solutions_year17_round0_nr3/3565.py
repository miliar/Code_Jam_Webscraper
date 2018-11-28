#include <stdio.h>
#include <queue>

using namespace std;

int main()
{
	int T;
	
	scanf("%d", &T);
	for (int w = 0; w < T; w++) {
		int N, K;

		scanf("%d %d", &N, &K);

		{
			priority_queue<int> q;
			q.push(N);

			int last_small, last_max;

			for (int i = 0; i < K; i++) {
				int v = q.top();
				q.pop();

				v--;
				last_small = v / 2;
				last_max = v / 2 + v % 2;

				if (v == 0)
					continue;
				q.push(last_small);
				q.push(last_max);
			}

			printf("Case #%d: %d %d\n", w+1, last_max, last_small);
		}
	}

	return 0;
}