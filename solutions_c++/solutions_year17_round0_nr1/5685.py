/*Oversized Pancake Flipper*/

#include<cstdio>
#include<cstring>
#include<queue>
#include<utility>

using namespace std;

int main()
{
	char S[16];
	bool visited[1024];
	bool found;
	int count, current, i, K, length, next, t, T;
	pair<int, int> p;
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%s %d", S, &K);
		length = strlen(S);
		current = 0;
		for (i = 0; i < length; i++)
			current = (current << 1) + ((S[i] == '-') ? 1 : 0);
		memset(visited, 0, sizeof(visited));
		queue< pair<int, int> > q;
		q.push(make_pair(current, 0));
		visited[current] = true;
		found = false;
		while (!q.empty())
		{
			p = q.front();
			q.pop();
			current = p.first;
			count = p.second;
			if (current == 0)
			{
				found = true;
				printf("Case #%d: %d\n", t, count);
				break;
			}
			for (i = 0; i < length - K + 1; i++)
			{
				next = current ^ ((1 << (i + K)) - (1 << i));
				if (!visited[next])
				{
					visited[next] = true;
					q.push(make_pair(next, count + 1));
				}
			}
		}
		if (!found)
			printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return 0;
}