#include <bits/stdc++.h>

#define MAX 5010
#define INF 0x3f3f3f3f
using namespace std;
typedef long long ll;


int dp[1450][725][2][2];
int notPossible[1450];
int t,n,m,x,y;

int solve(int curr, int tempo, int turn, int st)
{
	if (tempo > 720)
		return INF;
	if (curr == 1440 and tempo == 720)
	{
		return turn != st;
	}
	else if (curr == 1440)
		return INF;

	int & ret = dp[curr][tempo][turn][st];
	if (ret != -1)
		return ret;
	ret = INF;
	if (notPossible[curr] != turn)
		ret = solve(curr + 1, tempo + (turn == 0), turn, st);
	if (notPossible[curr] != (!turn))
		ret = min(ret, solve(curr + 1, tempo + ((!turn) == 0), !turn, st) + 1);
	return ret;
}

int main()
{
	scanf("%d",&t);
	for (int cases = 1; cases <= t; ++cases)
	{
		scanf("%d%d",&n,&m);
		memset(notPossible, -1, sizeof notPossible);
		memset(dp, -1, sizeof dp);
		for (int i = 0; i < n; ++i)
		{
			scanf("%d%d", &x, &y);
			for (int j = x; j < y; ++j)
			{
				notPossible[j] = 0;
			}
		}

		for (int i = 0; i < m; ++i)
		{
			scanf("%d%d", &x, &y);
			for (int j = x; j < y; ++j)
			{
				notPossible[j] = 1;
			}
		}

		printf("Case #%d: %d\n",cases, min(solve(0, 0, 0, 0), solve(0, 0, 1, 1)));
	}
	return 0;
}