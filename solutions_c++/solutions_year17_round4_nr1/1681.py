#include <bits/stdc++.h>

using namespace std;
const double pi=acos(-1.0);
const double eps=1e-9;
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define re return
#define vi vector <int> 
#define pii pair <int,int>
#define pll pair <long long , long long>
typedef long long ll;

int t, ans, cnt[10], n, p, a;

int main()
{
	ios:: sync_with_stdio(false);
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	cin >> t;
	for(int test = 1; test <= t; test++)
	{
		cin >> n >> p;
		ans = 0;
		for(int i = 0; i < 4; i++)
			cnt[i] = 0;
		for(int i = 0; i < n; i++)
		{
			cin >> a;
			cnt[a % p]++;
		}
		if(p == 2)
			ans = cnt[0] + cnt[1] / 2 + cnt[1] % 2;
		if(p == 3)
		{
			ans = cnt[0];
			ans += min(cnt[1], cnt[2]);
			ans += (max(cnt[1], cnt[2]) - min(cnt[1], cnt[2])) / 3;
			if((max(cnt[1], cnt[2]) - min(cnt[1], cnt[2])) % 3 != 0)ans++;
		}
		if(p == 4)
		{
			ans = cnt[0];
			ans += cnt[2] / 2;
			ans += min(cnt[1], cnt[3]);
			int rest = max(cnt[1], cnt[3]) - min(cnt[1], cnt[3]);
			if(cnt[2] % 2 == 1 && rest >= 2)
			{
				cnt[2] = 0;
				rest -= 2;
				ans++;
			}
			if(cnt[2] != 0 || rest % 4 != 0)ans++;
			ans += rest / 4;
		}
		cout << "Case #" << test << ": " << ans << "\n";
	}
	return 0;
}
