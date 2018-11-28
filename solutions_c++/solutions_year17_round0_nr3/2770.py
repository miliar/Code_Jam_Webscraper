#include<bits/stdc++.h>
using namespace std;
const bool DBG = 1;

#define TRACE(x)    x
#define WATCH(x)    TRACE(cout << #x" = " << x << endl)
#define WATCHR(a,b) TRACE(for(auto it=a; it!=b;) cout<<*(it++)<<" ";cout<<endl)
#define WATCHC(V)   TRACE({cout << #V" = "; WATCHR(V.begin(), V.end());})
#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<pair<int,int>> vpii;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	cout << fixed << setprecision(15);

	int T; cin >> T;
	ll n,k;
	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cin >> n >> k;

		ll cur = n;
		ll cntA = 1;
		ll cntB = 0;
		while(k > (cntA + cntB)) {
			k -= (cntA + cntB);
			if(cur % 2) {
				cntA = 2LL * cntA + cntB;
			} else {
				cntB = 2LL * cntB + cntA;
			}
			cur /= 2LL;
			//cout << cur << ":" << cntA << " | " << cur-1 << ":" << cntB << endl;
		}
		if(k > cntA) {
			ll gap = cur-1;
			if(gap % 2) {
				cout << (gap/2) << " " << (gap/2) << endl;
			} else {
				cout << (gap/2) << " " << (gap/2-1) << endl;
			}
		} else {
			ll gap = cur;
			if(gap % 2) {
				cout << (gap/2) << " " << (gap/2) << endl;
			} else {
				cout << (gap/2) << " " << (gap/2-1) << endl;
			}
		}
	}

	return 0;
}
