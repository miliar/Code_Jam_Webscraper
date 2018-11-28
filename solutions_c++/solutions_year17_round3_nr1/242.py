#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second

using namespace std;

typedef long long ll;
typedef pair<ll, ll> ii;

const int N = 1010;
const double PI = acos(-1.0);
const double oo = 1e15;



int main()
{
	int t, casecnt = 1;
	scanf("%d", &t);
	while(t--)
	{
		int n, k;
		vector<ii> pan;
		scanf("%d %d", &n, &k);
		for (int i = 0; i < n; i++)
		{
			int r, h;
			scanf("%d %d", &r, &h);
			pan.pb(ii((ll)r, (ll)h));
		}
		ll ans = 0;
		for (int i = 0; i < n; i++)
		{
			ll top = pan[i].fi * pan[i].fi;
			ll side = 2 * pan[i].fi * pan[i].se;
			
			vector<ll> pan2;
			for (int j = 0; j < n; j++)
			{
				if (j == i) continue;

				if (pan[j].fi <= pan[i].fi)
					pan2.pb(2 * pan[j].fi * pan[j].se);
			}
			if (pan2.size() < k-1) continue;
			sort(pan2.begin(), pan2.end());
			reverse(pan2.begin(), pan2.end());
			for (int j = 0; j < k-1; j++)
				side += pan2[j];
			//printf("i = %d: top = %lf, side = %lf\n", i, top, side);
			ans = max(ans, top+side);
		}
		printf("Case #%d: %.9lf\n", casecnt++, ans * PI);
	}
	return 0;
}


