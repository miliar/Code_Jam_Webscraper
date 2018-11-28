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
	string s;
	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cin >> s;
		for(int i = s.size()-2; i >= 0; i--) {
			if(s[i] > s[i+1]) {
				s[i]--;
				for(int j = i+1; j < s.size(); j++) {
					s[j] = '9';
				}
			}
		}
		ll ans;
		stringstream ss; ss << s; ss >> ans;
		cout << ans << endl;
	}

	return 0;
}
