#include <bits/stdc++.h>
using namespace std; 
int c[100010], a[100100], ans, n, m, T; 
int main()
{
	freopen("a.in", "r", stdin); 
	freopen("a.out", "w", stdout); 
	cin >> T; 
	for (int Cs = 1; Cs <= T; Cs++) 
	{
		memset(c, 0, sizeof(c)); 
		cin >> n >> m; 
		for (int i = 1; i <= n; i++) 
		{
			cin >> a[i];
			c[a[i] % m]++; 
		}
		if (m == 2) {
			ans = c[0] + (c[1] + 1) / 2; 
		}
		else if (m == 3) {
			ans = c[0]; 
			int t = min(c[1], c[2]); 
			c[1] -= t; c[2] -= t; 
			ans += t + (c[1] + c[2] + 2) / 3; 
		}
		else 
		{
			ans = c[0]; 
			int t = min(c[1], c[3]); 
			ans += (c[2]) / 2 + t / 2;
			c[2] -= c[2] / 2 * 2; 
			c[1] -= t; c[3] -= t; 
			if (!c[1] && c[2] && !c[3]) {
				ans++; 
			}
			else if (c[1] && !c[2]) {
				ans += (c[1] + 3) / 4; 
			}
			else if (c[3] && !c[2]) { 
				ans += (c[3] + 3) / 4; 
			}
			else if ((c[1] + c[3]) && c[2]) 
			{
				ans ++; 
				ans += max(0, (c[1] + c[3] + 1)/ 4); 
			}
		}
		printf("Case #%d: %d\n", Cs, ans); 
	}
	return 0; 
}
