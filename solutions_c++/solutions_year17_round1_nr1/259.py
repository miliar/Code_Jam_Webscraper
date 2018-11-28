#include <bits/stdc++.h>
using namespace std;
#define rep(it,st,en) for(int it=(st);it<(int)(en);++it)
#define allof(c) (c).begin(), (c).end()
#define mt make_tuple
#define mp make_pair
#define pb push_back
#define X first
#define Y second
typedef long long int ll; 
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
const int INF=(int)1e9; 
const double EPS=(ld)1e-7;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    rep(t,1,T+1){
        int r,c;
        cin>>r>>c;
        vector<string> s(r);
        rep(i,0,r) cin>>s[i];
        string ss = s[0];
        int k = 1e9;
        rep(i,0,r){
            rep(j,0,c) {
                if(s[i][j] != '?') {
                    s[i][0] = s[i][j];
                    break;
                }
            }
            if(s[i][0] != '?'){
                k = min(i,k);
                rep(j,1,c) if(s[i][j] == '?') s[i][j] = s[i][j-1];
                ss = s[i];
            }
            else s[i] = ss;
        }
        cout<<"Case #"<<t<<": "<<endl;
        rep(i,0,r){
            if(i < k) cout<<s[k]<<'\n';
            else cout<<s[i]<<'\n';
        }
        cout<<flush;
    }
    return 0;
}
