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
		string s; int k;
		cin >> s >> k;
		int ans = 0;
		FOR(i,0,(int)s.size()-k+1) {
			if (s[i] == '-') {
				ans++;
				FOR(j,i,i+k) {
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		bool flag = true;
		FOR(i,(int)s.size()-k, (int)s.size())
			if (s[i] == '-') flag = false;
		cout << "Case #" << t << ": ";
		if (flag) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}