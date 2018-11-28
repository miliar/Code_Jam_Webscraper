#include <bits/stdc++.h>

#define ll long long
using namespace std;

const int MAXN = 200005;
const int MOD = 1000000007;

int main(){
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for(int tc = 1; tc <= T; tc++){
		cout << "Case #" << tc << ": ";
		ll n;
		long double d;
		cin >> d >> n;
		long double ans = 1e17;
		for(int i=0;i<n;i++){
			long double k,s;
			cin >> k >> s;
			long double temp = s * d / (d - k);
			ans = min(ans,temp);
		}
		cout << setprecision(12) << fixed << ans << '\n';
	}
	return 0;
}

