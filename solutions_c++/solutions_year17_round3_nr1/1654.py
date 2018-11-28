/*
* @Author: Hasit Bhatt
* @Date:   2017-04-30 14:27:37
* @Last Modified by:   hasit
* @Last Modified time: 2017-04-30 15:37:08
*/

#include <bits/stdc++.h>

using namespace std;

typedef int ll;
typedef long double ld;

vector< pair<ll,ll> > v;
vector< vector<ld> > k;

int N,K,a,b;

long double solve(int last, int remaining) {
	long double ans = LDBL_MIN;
	ld a = -1;
	if(remaining == 0) {
		return 0;
	}
	if(last+1 < remaining)
		return ans;
	if(k[last][remaining-1] != a) {
		return k[last][remaining-1];
	} else {
		ans = solve(last - 1, remaining);
		//cout << last << " " << remaining << " A " << ans << endl;
		long double including = 1;
		long double z = 1;
		including = including * 2 * M_PI * v[last].first * v[last].second;
		including += solve(last - 1,remaining - 1);
		if(remaining == K) {
			//cout << last << " " << remaining << " B " << including << endl;
			//cout << v[last].first << endl;
			including += ld(1) * M_PI * v[last].first * v[last].first;
			//cout << last << " " << remaining << " B " << including << endl;
		}
		ans = max(ans, including);
	}
	return k[last][remaining-1] = ans;
}

void solve() {
	v.clear();
	k.clear();
	cin >> N >> K;
	v.resize(N);
	k.resize(N,vector<ld>(K,-1));
	for(int i=0;i<N;i++) {
		cin >> a >> b;
		v[i] = make_pair(a,b);
	}
	sort(v.begin(),v.end());
	long double surface = 1;
	surface = surface * M_PI * v[N-1].first * v[N-1].first;
	long double ans = solve(N-1,K);
	cout << fixed << setprecision(9);
	cout << ans;
}

int main(){
	int n;
	cin >> n;
	for(int i=1;i<=n;i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
    return 0;
}