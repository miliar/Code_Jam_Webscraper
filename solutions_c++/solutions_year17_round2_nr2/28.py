#include <bits/stdc++.h>

using namespace std;

#define REP(i, a, b) for (int i = (a), i##_end_ = (b); i < i##_end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

typedef long long LL;

const int oo = 0x3f3f3f3f;

const int maxn = 1010;

char a[maxn + 5];

bool work(int n, int R, int O, int Y, int G, int B, int V)
{
	//R, G
	//Y, V
	//B, O
	if (R == G && R + G == n)
	{
		REP(i, 0, n) if (i & 1) a[i] = 'R'; else a[i] = 'G';
		return 1;
	}
	if (Y == V && Y + V == n)
	{
		REP(i, 0, n) if (i & 1) a[i] = 'Y'; else a[i] = 'V';
		return 1;
	}
	if (B == O && B + O == n)
	{
		REP(i, 0, n) if (i & 1) a[i] = 'B'; else a[i] = 'O';
		return 1;
	}
	if (G && R <= G) return 0;
	if (V && Y <= V) return 0;
	if (O && B <= O) return 0;
	R -= G, Y -= V, B -= O;
	int num[3] = {R, Y, B};
	int pos[3] = {0, 1, 2};
	swap(pos[0], pos[max_element(num, num + 3) - num]);
	if (num[pos[0]] > num[pos[1]] + num[pos[2]]) return 0;
	static vector<int> b[maxn + 5];
	REP(i, 0, num[pos[0]]) b[i].clear(), b[i].pb(pos[0]);
	int now = -1;
	REP(i, 0, num[pos[1]]) b[(++now) %= num[pos[0]]].pb(pos[1]);
	REP(i, 0, num[pos[2]]) b[(++now) %= num[pos[0]]].pb(pos[2]);
	int an = 0;
	REP(i, 0, num[pos[0]])
	{
		for (auto u : b[i])
		{
			if (u == 0)
			{
				if (G) 
				{
					REP(j, 0, G) a[an++] = 'R', a[an++] = 'G';
					G = 0;
				}
				a[an++] = 'R';
			}
			if (u == 1)
			{
				if (V) 
				{
					REP(j, 0, V) a[an++] = 'Y', a[an++] = 'V';
					V = 0;
				}
				a[an++] = 'Y';
			}
			if (u == 2)
			{
				if (O) 
				{
					REP(j, 0, O) a[an++] = 'B', a[an++] = 'O';
					O = 0;
				}
				a[an++] = 'B';
			}
		}
	}
	return 1;
}

int main()
{
#ifdef matthew99
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int n;
	int R, O, Y, G, B, V;
	int case_cnt;
	scanf("%d", &case_cnt);
	for (int case_id = 1; case_id <= case_cnt; ++case_id)
	{
		printf("Case #%d: ", case_id);
		scanf("%d%d%d%d%d%d%d", &n, &R, &O, &Y, &G, &B, &V);
		int tmp = work(n, R, O, Y, G, B, V);
		a[n] = 0;
		if (!tmp) { puts("IMPOSSIBLE"); continue; }
		else puts(a);
		int cntR = 0, cntO = 0, cntY = 0, cntG = 0, cntB = 0, cntV = 0;
		static int b[maxn + 5];
		REP(i, 0, n)
		{
			if (a[i] == 'R') b[i] = 1, ++cntR;
			if (a[i] == 'Y') b[i] = 2, ++cntY;
			if (a[i] == 'B') b[i] = 4, ++cntB;
			if (a[i] == 'O') b[i] = 1 | 2, ++cntO;
			if (a[i] == 'G') b[i] = 2 | 4, ++cntG;
			if (a[i] == 'V') b[i] = 1 | 4, ++cntV;
		}
		if (cntR != R || cntO != O || cntY != Y || cntG != G || cntB != B || cntV != V)
		{
			debug("%d %d %d %d %d %d wrong number\n", R, O, Y, G, B, V);
			exit(1);
		}
		else
		{
			REP(i, 0, n) if (b[i] & b[(i + 1) % n]) 
			{
				debug("%d %d %d %d %d %d wrong sequence\n", R, O, Y, G, B, V);
				exit(1);
			}
		}
	}
	return 0;
}
