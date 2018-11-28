#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii > vii;
typedef vector<vector<int> > vvi;
typedef vector<vector<pair<int, int> > > vvii;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,s,e) for(int i=(s);i<(e);++i)
#define repr(i,s,e) for(int i=(e);i>(s);--i)

const ll MOD = 1e9+7;
const ll INF = 1e14;
const ll TE3 = 1005;
const ll TE5 = 100005;
// ll m[2] = {1000000007ll, 1000000009ll};

// ll hash_str(string s) {
// 	ll h[2] = {0ll, 0ll};
// 	for (char c : s) fo(i, 0, 2) h[i] = (h[i] * 137 + c) % m[i];
// 	return h[0] * 1000000009ll + h[1];
// }

int main() {
    ios::sync_with_stdio(false);
    int t, k;
    cin>>t;
    rep(i,1,t+1) {
        string s;
        cin>>s>>k;
        int l = s.size(), c=0;
        rep(j,0,l-k+1) {
            if(s[j] == '+') continue;
            c++;
            rep(pp,0,k) {
                s[j+pp] = (s[j+pp]=='-')?'+':'-';
            }
        }
        int fl = 0;
        rep(j,0,l) {
            if(s[j]=='-') {
                cout<<"Case #"<<i<<": IMPOSSIBLE\n";
                fl = 1;
                break;
            }
        }
        if(!fl) {
            cout<<"Case #"<<i<<": "<<c<<'\n';
        }
    }
    return 0;
}