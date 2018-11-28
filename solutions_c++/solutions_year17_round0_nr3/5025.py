#include <stdio.h>
#include <queue>

using namespace std;

int main ()
{
	priority_queue<int> p;
	int n, k, m;
	scanf("%d", &n);
	
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		scanf("%d%d", &k, &m);
		for (int j = 0; j < m; j++)
		{
			// printf("%d\n", k);
			if (k % 2 == 0)
			{
				if (j == m - 1)
					printf("%d %d\n", k/2, k/2 - 1);
				p.push (k/2);
				p.push (k/2 - 1);
			}
			else
			{
				if (j == m - 1)
					printf("%d %d\n", k/2, k/2);
				p.push (k/2);
				p.push (k/2);
			}
			k = p.top();
			p.pop();
		}
		while (!p.empty())
			p.pop();
	}

	return 0;
}