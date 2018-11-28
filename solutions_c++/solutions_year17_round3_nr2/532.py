#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define INF (1111111)
#define maxn 1555

typedef long long ll;

ll dp[3][3][3][maxn][2 * maxn];
ll day[2000];

ll fun(ll zac, ll kon, ll last, ll x, ll raz){
	if(x == 1439 && raz == maxn)
		return (1 - (kon == last));
	if(x == 1439)
		return INF;

	ll &cur = dp[zac][kon][last][x][raz];
	if(cur != -1)
		return cur;

	cur = INF;

	if(day[x] == 0){
		cur = min(cur, fun(zac, kon, 0, x + 1, raz - 1) + 1 - (0 == last));
	}

	if(day[x] == 1){
		cur = min(cur, fun(zac, kon, 1, x + 1, raz + 1) + 1 - (1 == last));
	}

	if(day[x] == -1){
		cur = min(cur, fun(zac, kon, 1, x + 1, raz + 1) + 1 - (1 == last));
		cur = min(cur, fun(zac, kon, 0, x + 1, raz - 1) + 1 - (0 == last));
	}

	return cur;
}

ll solve(){
	memset(dp, -1, sizeof(dp));
	memset(day, -1, sizeof(day));

	ll c, j;
	cin >> c >> j;
	for(ll i = 0; i < c; i++){
		ll a, b;
		cin >> a >> b;
		for(ll j = a; j < b; j++){
			day[j] = 0;
		}
	}

	for(ll i = 0; i < j; i++){
		ll a, b;
		cin >> a >> b;
		for(ll k = a; k < b; k++){
			day[k] = 1;
		}
	}

	ll ans = INF;
	for(ll i = 0; i < 2; i++){
		for(ll j = 0; j < 2; j++){
		ll x = INF;
		ll d0 = (i == 0) + (j == 0);
		ll d1 = (i == 1) + (j == 1);
		if((day[0] == i || day[0] == -1) && (day[1439] == j || day[1439] == -1)){
			x = fun(i, j, i, 1, maxn + d1 - d0);
		}

		if(i != j)
			x++;

		ans = min(ans, x);
		}

	}
	return ans;
}



int main(){
	ll t;
	cin >> t;
	for(ll ll = 1; ll <= t; ll++){
		cout << "Case #" << ll << ": " << solve() << endl;
	}
	return 0;
}