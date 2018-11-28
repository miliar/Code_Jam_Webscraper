#include<bits/stdc++.h>
using namespace std;
#define FOR(i,s,e) for(int i = (s); i < (e); i++)
#define FOE(i,s,e) for(int i = (s); i <= (e); i++)
#define FOD(i,s,e) for(int i = (s); i >= (e); i--)
#define ll long long
#define pb push_back

int n, m, x, y, z, k, w;
int a, b, c, d, e, f;
int tc, tt;
int A[1005], ans[1005];

void output()
{
	FOR(i, 0, n) 
	{
		if (ans[i] == 1) printf("R");
		if (ans[i] == 2) printf("Y");
		if (ans[i] == 3) printf("B");
	}
	printf("\n");
}

int main ()
{
	scanf("%d", &tc);
	while (tc--)
	{
		scanf("%d %d %d %d %d %d %d", &n, &a, &b, &c, &d, &e, &f);
		
		printf("Case #%d: ", ++tt);
	
		w = 0;
		for (int i = 0; i < n; i += 2) A[w++] = i;
		for (int i = 1; i < n; i += 2) A[w++] = i;
		
		memset(ans, 0, sizeof(ans));
		
		if (a >= c && a >= e) 
		{
			FOR(i, 0, a) ans[A[i]] = 1;
			FOR(i, a, a + c) ans[A[i]] = 2;
			FOR(i, a + c, a + c + e) ans[A[i]] = 3;
		}
		else if (c >= a && c >= e)
		{
			FOR(i, 0, c) ans[A[i]] = 2;
			FOR(i, c, a + c) ans[A[i]] = 1;
			FOR(i, a + c, a + c + e) ans[A[i]] = 3;
		}
		else 
		{
			FOR(i, 0, e) ans[A[i]] = 3;
			FOR(i, e, a + e) ans[A[i]] = 1;
			FOR(i, a + e, a + e + c) ans[A[i]] = 2;
		}
		
		x = 1;
		ans[n] = ans[0];
		FOE(i, 1, n) if (ans[i] == ans[i - 1]) x = 0;
	
		if (x == 0) printf("IMPOSSIBLE\n");
		else output();
	}
	
	return 0;
}
