#include <bits/stdc++.h>
using namespace std;
#define eb emplace_back
#define emp emplace
#define fi first
#define se second
#define INF 0x3f3f3f3f
typedef long long ll;
typedef pair<int,int> ii;

const int GAMB = 11234;
ll n, p;
ll serv[51];
ll ing[51][51], used[51][51];
vector<ll> has_ing[51][GAMB];

int main(void) {
	ios_base::sync_with_stdio(false);
	int t; cin >> t;

	int cnt = 1;
	while (t--) {
		memset(serv, 0, sizeof serv);
		memset(ing, 0, sizeof ing);
		memset(used, 0, sizeof used);
		for (int i = 0; i < 51; i++) for (int j = 0; j <= GAMB; j++) has_ing[i][j].clear();
		cin >> n >> p;
		for (int i = 0; i < n; i++)	cin >> serv[i];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < p; j++)	cin >> ing[i][j];
			sort(ing[i], ing[i]+p);
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < p; j++)	{
				for (int k = 1; k <= GAMB; k++) {
					if (10*ing[i][j] >= 9*serv[i]*k and 10*ing[i][j] <= 11*serv[i]*k) {
						has_ing[i][k].eb(j);
					}
				}
			}
		}

		ll ans = 0;
		for (int i = 1; i <= GAMB; i++) {
			int mini = INF;
			for (int j = 0; j < n; j++)	{
				int ct = 0;
				for (int k = 0; k < has_ing[j][i].size(); k++) if (!used[j][has_ing[j][i][k]]) ct++;
				mini = min(mini, ct);
			}

			for (int j = 0; j < n; j++) {
				int ct = 0;
				for (int k = 0; k < has_ing[j][i].size() && ct < mini; k++) {
					int id = has_ing[j][i][k];
					if (!used[j][id]) {
						used[j][id] = 1;
						ct++;
					}
				}
			}
			ans += mini;
		}

		cout << "Case #" << cnt++ << ": " << ans << endl;
	}
    
	return 0;
}
