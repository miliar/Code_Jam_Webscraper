#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(ll i=0; i<(ll)(n); i++)
#define FOR(i,n,m) for (ll i=n; i<(ll)(m); i++)
#define pb push_back
#define INF 1000000007LL
#define all(a) (a).begin(),(a).end()
#define chmin(a,b) a=min(a,b)
#define chmax(a,b) a=max(a,b)

typedef long long ll;
typedef pair<int,int> p;

int dy[4]={-1,1,0,0};
int dx[4]={0,0,1,-1};


ll makeTidy(ll n) {
    string S = to_string(n);
    vector<int> a;
    REP(i,S.length()) {
        a.pb(S[i]-'0');
    }
    bool f=1;
    while(f) {
        f=0;
        REP(i, a.size()-1) {
            if(a[i]>a[i+1]) {
                f=1;
                a[i]--;
                FOR(j,i+1,a.size()) {
                    a[j]=9;
                }
            }
        }
    }
    ll ret = 0;
    REP(i,a.size()) {
        ret*=10;
        ret+=a[i];
    }
    return ret;
}

int main(){
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    REP(c,T) {
        ll N;
        cin >> N;
        cout << "Case #" << c+1 << ": "<< makeTidy(N) << endl;
    }
    return 0;
}
