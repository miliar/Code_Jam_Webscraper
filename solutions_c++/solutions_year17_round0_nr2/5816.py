#include <bits/stdc++.h>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define fst first
#define snd second
#define debug(x) cout << #x << " = " << x << endl;
typedef long long ll;
typedef pair<int, int> ii;

const ll SZ = 1e18;

ll n;
vector<ll> vet;

void solve(ll s){
	if(s > SZ)
		return;
	vet.pb(s);
	for(int i = 0; i <= 9; i++){
		if(s == 0){
			if(i)
				solve(i);
		}
		else if((s % 10) <= i)
			solve(s * 10LL + i);
	}
}

int main(){
	freopen("B.in", "rt", stdin);
	freopen("B.out", "wt", stdout);

	solve(0);
	sort(all(vet));

	int T;
	cin >> T;
	for(int tt = 1; tt <= T; tt++){
		cin >> n;
		printf("Case #%d: ", tt);

		int l = 0, r = vet.size() - 1;
		ll ans = 1;
		while(l <= r){
			int mid = (l + r) / 2;
			if(vet[mid] <= n){
				ans = vet[mid];
				l = mid + 1;
			}
			else
				r = mid - 1;
		}
		cout << ans << endl;
	}
	return 0;
}