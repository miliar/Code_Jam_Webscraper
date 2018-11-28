#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
const ld EPS = 1e-9;
const ll MOD = 1e9 + 7;

int dcmp(ld x, ld y) {
	return fabs(x-y) <= EPS ? 0 : x < y ? -1 : 1;
}

ll n;vector<ld> sps;
ld d;vector<ld> pos;

bool valid(ld sp) {
	ld tm = d/sp;
	for(int i=0;i<n;++i) {
		ld tmp = (tm * sps[i]) + pos[i];
		if(dcmp(tmp,tm*sp)==-1) return 0;
	}
	return 1;
}


ld DBS2(ld s,ld e) {
	for(int i=0;i<1000;++i) {
		ld mid = (s + e)/2;
		if(valid(mid))
			s = mid;
		else
			e = mid;
	}
	if(valid(s)) return e;
	return -1;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;cin >> T;
	for(int t=1;t<=T;++t) {
		cin >> d >> n;
		pos = vector<ld>(n);
		sps = vector<ld>(n);
		for(int i=0;i<n;++i)
			cin >> pos[i] >> sps[i];

		ld ans = DBS2(0.00000001,(ld)1e15);
		cout << "Case #"<<t<<": "<<setprecision(8) << fixed << ans << endl;


	}
}
