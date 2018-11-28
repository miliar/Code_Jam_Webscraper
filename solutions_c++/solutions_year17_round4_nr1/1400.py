#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int N = 101;
int pd2[N][N][2];
int pd3[N][N][N][3];
int pd4[N][N][N][N][4];
const int oo = 0x3f3f3f3f;

int solve2(int g0, int g1, int left)
{
	if (g0 < 0 or g1 < 0)
		return -oo;
	
	if (g0 + g1 == 0)
		return 0;

	int& ret = pd2[g0][g1][left];
	if (ret != -1)
		return ret;


	ret = -oo;

	const int P = 2;
	int g, newg, newleft;
	int noleft = (left == 0);

	g = 0;
	newg = (P + g - left)%P;
	newleft = (P - newg)%P;
	ret = max(ret, noleft + solve2(g0-1, g1, newleft));

	g = 1;
	newg = (P + g - left)%P;
	newleft = (P - newg)%P;
	ret = max(ret, noleft + solve2(g0, g1-1, newleft));
	return ret;
}

int solve3(int g0, int g1, int g2, int left)
{
	if (g0 < 0 or g1 < 0 or g2 < 0)
		return -oo;
	
	if (g0 + g1 + g2 == 0)
		return 0;

	int& ret = pd3[g0][g1][g2][left];
	if (ret != -1)
		return ret;


	ret = -oo;

	const int P = 3;
	int g, newg, newleft;
	int noleft = (left == 0);

	g = 0;
	newg = (P + g - left)%P;
	newleft = (P - newg)%P;
	ret = max(ret, noleft + solve3(g0-1, g1, g2, newleft));

	g = 1;
	newg = (P + g - left)%P;
	newleft = (P - newg)%P;
	ret = max(ret, noleft + solve3(g0, g1-1, g2, newleft));

	g = 2;
	newg = (P + g - left)%P;
	newleft = (P - newg)%P;
	ret = max(ret, noleft + solve3(g0, g1, g2-1, newleft));

	return ret;
}

int solve4(int g0, int g1, int g2, int g3, int left)
{
	if (g0 < 0 or g1 < 0 or g2 < 0 or g3 < 0)
		return -oo;
	
	if (g0 + g1 + g2 + g3 == 0)
		return 0;

	int& ret = pd4[g0][g1][g2][g3][left];
	if (ret != -1)
		return ret;

	ret = -oo;

	const int P = 4;
	int g, newg, newleft;
	int noleft = (left == 0);

	g = 0;
	newg = (P + g - left)%P;
	newleft = (P - newg)%P;
	ret = max(ret, noleft + solve4(g0-1, g1, g2, g3, newleft));

	g = 1;
	newg = (P + g - left)%P;
	newleft = (P - newg)%P;
	ret = max(ret, noleft + solve4(g0, g1-1, g2, g3, newleft));

	g = 2;
	newg = (P + g - left)%P;
	newleft = (P - newg)%P;
	ret = max(ret, noleft + solve4(g0, g1, g2-1, g3, newleft));

	g = 3;
	newg = (P + g - left)%P;
	newleft = (P - newg)%P;
	ret = max(ret, noleft + solve4(g0, g1, g2, g3-1, newleft));

	return ret;
}
int main()
{
	memset(pd2, -1, sizeof(pd2));
	memset(pd3, -1, sizeof(pd3));
	memset(pd4, -1, sizeof(pd4));

	int t, casecnt=1;
	scanf("%d", &t);
	while(t--)
	{
		int n, p;
		int g[4] = {0};
		scanf("%d %d", &n, &p);
		for (int i = 0; i < n; i++)
		{
			int x;
			scanf("%d", &x);
			g[x%p]++;
		}
		printf("Case #%d: ", casecnt++);
		
		int ans = -1;
		if (p == 2)
			ans = solve2(g[0], g[1], 0);
		else if (p == 3)
			ans = solve3(g[0], g[1], g[2], 0);
		else if (p == 4)
			ans = solve4(g[0], g[1], g[2], g[3], 0);

		printf("%d\n", ans);
	}

	return 0;
}


