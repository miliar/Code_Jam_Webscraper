#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
using namespace std;
int x;
int W[3001][3001];
int P[3001];
bool V[3001];
int N, C, M;
void check()
{
	vector<int> p;
	int x = N + N + 1;
	int Min = -1;
	p.push_back(x);
	while(x != 0)
	{
		if(Min == -1) Min = W[P[x]][x];
		else Min = min(Min, W[P[x]][x]);
		x = P[x];
		p.push_back(x);
	}
	for(int i = 0; i< p.size() - 1; i++)
	{
		W[p[i]][p[i + 1]] += Min;
		W[p[i + 1]][p[i]] -= Min;
	}
}
bool process()
{
	queue<int> q;
	q.push(0);
	memset(V, 0, sizeof(V));
	V[0] = true;
	int S, E;
	while(!q.empty())
	{
		int x = q.front();
		q.pop();
		if(x == N + N + 1)
		{
			break;
		}
		if(x == 0 || (N + 1 <= x && x <= N + N)) S = 1, E = N;
		else S = N + 1, E = N + N;
		if(W[x][N + N + 1] && !V[N + N + 1])
		{
			V[N + N + 1] = true;
			P[N + N + 1] = x;
			break;
		}
		for(int i = S; i <= E; i++)
		{
			if(V[i]) continue;
			if(!W[x][i]) continue;
			V[i] = true;
			P[i] = x;
			q.push(i);
		}
	}
	if(V[N + N + 1])
	{
		check();
		return true;
	}
	return false;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d %d %d", &N, &C, &M);
		memset(W, 0, sizeof(W));
		int A = 0, B = 0;
		for(int i = 1; i <= M; i++)
		{
			int x, y;
			scanf("%d %d", &x, &y);
			if(y == 1) {
				A++;
				W[0][x]++;
			} else {
				B++;
				W[N + x][N + N + 1]++;
			}
		}
		for(int i = 1; i <= N; i++)
		{
			for(int j = 1; j <= N; j++)
			{
				if(i == j) continue;
				W[i][N + j] = 10000;
			}
		}
		while(process()) {}
		int c1 = 0, c2 = 0, c = 0, cc = 0;
		for(int i = 1; i <= N; i++)
		{
			c1 += W[0][i];
			if(W[0][i]) cc = i;
			c2 += W[N + i][N + N + 1];
			c += W[i][0];
		}
		int S = c, Promote = 0;
		if(c1 != 0 && c2 != 0 && cc == 1) S += c1 + c2;
		else if(c1 != 0 && c2 != 0)
		{
			Promote = min(c1, c2);
			S += max(c1, c2);
		}
		else S += c1 + c2;
		printf("Case #%d: %d %d\n", t, S, Promote);
	}
}