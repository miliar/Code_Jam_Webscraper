#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int N = 1450;

int pd[N][725][2][2];
int p[2][N];

const int oo = 0x3f3f3f3f;


int solve(int pos, int rem, int parent, int first)
{
	if (rem < 0)
		return oo;
	
	if (pos - (720 - rem) > 720)
		return oo;
	
	if (pos == 1440)
	{
		//printf("rem = %d\n", rem);
		if (rem != 0)
			return oo;

		if (parent != first)
			return 1;
		return 0;
	}

	int& ret = pd[pos][rem][parent][first];
	if (ret != -1)
		return ret;

	ret = oo;
	if (p[parent][pos] == 0)
	{
		if (parent == 0)
			ret = min(ret, solve(pos+1, rem-1, parent, first)); 
		else
			ret = min(ret, solve(pos+1, rem, parent, first));
	}
	if (p[!parent][pos] == 0)
	{
		if (parent == 0)
			ret = min(ret, 1 + solve(pos+1, rem, !parent, first));
		else
			ret = min(ret, 1 + solve(pos+1, rem-1, !parent, first));
	}
	return ret;
}


int main()
{
	int t, casecnt = 1;
	scanf("%d", &t);
	while(t--)
	{
		memset(p, 0, sizeof(p));

		int ac, aj;
		scanf("%d %d", &ac, &aj);
		for (int i = 0; i < ac; i++)
		{
			int c, d;
			scanf("%d %d", &c, &d);
			for (int j = c; j < d; j++)
				p[0][j] = 1;
		}
		for (int i = 0; i < aj; i++)
		{
			int c, d;
			scanf("%d %d", &c, &d);
			for (int j = c; j < d; j++)
				p[1][j] = 1;
		}
		memset(pd, -1, sizeof(pd));
		int ans = min(solve(0, 720, 0, 0), solve(0, 720, 1, 1));

		printf("Case #%d: %d\n", casecnt++, ans);
	}
	return 0;
}
