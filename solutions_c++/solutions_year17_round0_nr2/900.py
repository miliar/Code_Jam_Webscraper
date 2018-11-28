#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;
typedef pair<int, ll> pil;
typedef pair<ll, int> pli;
typedef vector<int> VI;
#define pb push_back
#define xx first
#define yy second
#define FOR(i,a,b) for(int i=a;i<int(b);i++)
#define FORB(i,a,b) for(int i=int(b)-1;i>=int(a);i--)
	
int main() {
	int T; cin >> T;
	FOR(t,1,T+1) {
		string s; cin >> s;
		string ans = s;
		FOR(i,1,s.size()) {
			if (ans[i] < ans[i-1]) { 
				ans[i-1]--;
				FOR(k,i,s.size()) ans[k] = '9';
				FORB(j,1,i) {
					if (ans[j] < ans[j-1]) {
						ans[j-1]--;
						FOR(k,j,s.size()) ans[k] = '9';
					}
				}
			}
		}
		cout << "Case #" << t << ": ";
		bool lz = true;
		FOR(i,0,ans.size()) {
			if (ans[i] != '0') lz = false;
			if (ans[i] == '0') {
				if (!lz) cout << ans[i];
			} else {
				cout << ans[i];
			}
		}
		cout << endl;
	}
	return 0;
}