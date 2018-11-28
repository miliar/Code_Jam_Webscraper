#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int maxN = 1e3 + 7;
 
int n, c, t;
int N[maxN], C[maxN];
int add[maxN];

int main()
{
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int tt = 0; tt < T; tt++)
	{
		cout << "Case #" << tt+1 << ": ";
		memset(C, 0, sizeof C);
		memset(N, 0, sizeof N);
		memset(add, 0, sizeof add);
		cin >> n >> c >> t;
		while (t--)
		{
			int a, b;
			cin >> a >> b;
			a--, b--;
			N[a]++;
			C[b]++;
		}
		int ans = 0;
		for (int i=0; i<c; i++)
			ans = max(ans, C[i]);
		int sum = 0;
		for (int i=0; i<n; i++)
		{
			sum += N[i];
			ans = max(ans, (sum + i) / (i+1));
		}
		int res = 0;
		for (int i=n-1; i>=0; i--)
			if (N[i] + add[i] > ans)
			{
				int need = N[i] + add[i] - ans;
				int mn = min(need, add[i]);
				add[i-1] += mn;
				add[i] -= mn;
				need -= mn;
				res += need;
				N[i] -= need;
				add[i-1] += need;
			}
		cout << ans << " " << res << "\n";
	}

	return 0;
}
