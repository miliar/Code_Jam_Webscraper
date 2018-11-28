#include <bits/stdc++.h>
#define db double
#define N 100
#define eps 1e-14
using namespace std; 
int T, n, k; 
db U, a[N], ans;
bool ok(db x) 
{
	db s = 0; 
	for (int i = 1; i <= n; i++) 
		if (a[i] < x) s += x - a[i]; 
	return s <= U; 
}
int main()
{
	freopen("c.in", "r", stdin); 
	freopen("c.out", "w", stdout); 
	cin >> T; 
	for (int Cs = 1; Cs <= T; Cs++)
	{
		cin >> n >> k >> U; 
		for (int i = 1; i <= n; i++) 
			scanf("%lf", &a[i]); 
		db l = 0, r = 1; 
		while (r - l > eps) 
		{
			db mid = (l + r) / 2; 
			if (ok(mid)) l = mid; 
			else r = mid; 
		}
		for (int i = 1; i <= n; i++) 
			if (a[i] < l) a[i] = l; 
		ans = 1; 
		for (int i = 1; i <= n; i++) 
			ans *= a[i]; 
		printf("Case #%d: %.10lf\n", Cs, ans); 
	}
	return 0; 
}
