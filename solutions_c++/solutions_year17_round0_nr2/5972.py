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

int main() {
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    rep(j,1,t+1) {
        string s;
        cin>>s;
        int l = s.size(), r=-1, g=-1;
        rep(i,0,l-1) {
            if(s[i] == s[i+1] && r == -1) {
                r = i;
            }
            else if(s[i] > s[i+1]) {
                g = i;
                break;
            }
        }
        if(g == -1) {
            cout<<"Case #"<<j<<": ";
            rep(i,0,l) {
                if(s[i]=='0' && i == 0) {
                    continue;
                }
                cout<<s[i];
            }
            cout<<'\n';
            continue;
        }
        if(r == -1)
            r = g;
        s[r]--;
        rep(i,r+1, l) {
            s[i]='9';
        }
        cout<<"Case #"<<j<<": ";
        rep(i,0,l) {
            if(s[i] == '0' && i == 0) {
                continue;
            }
            cout<<s[i];
        }
        cout<<'\n';
    }
    return 0;
}