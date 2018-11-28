#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for(int i=0; i<int(n); ++i)
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
typedef long long ll;


int TC;
void solve() {
	string s;
	cin >> s;
	for(int i=sz(s); i>=1; i--) {
		string a = s;
		if (a[i-1] == '0') continue;
		if (i != sz(s)) a[i-1] = a[i-1] - 1;
		for(int j=i; j<sz(a); j++) a[j] = '9';
		bool ok = true;
		rep(j, sz(a)-1) if (a[j] > a[j+1]) ok = false;
		if (ok) {
			if (a[0] == '0') a = a.substr(1);
			cout << a << endl;
			return;
		}
	}
	assert(false);
}
int main() {
	int T; cin >> T;
	for(int TC=1; TC<=T; TC++) {
		cout << "Case #" << TC << ": ";
		solve();
	}
}

