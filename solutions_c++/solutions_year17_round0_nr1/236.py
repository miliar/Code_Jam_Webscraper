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
        string s;
        int k;
        cin>>s>>k;
        int ans=0;
        vector<int> v(s.size(),0);
        int x = 0;
        rep(i,0,s.size()){
            if((s[i] == '-') ^ x){
                if(i+k > s.size()){
                    ans = -1;
                    break;
                }
                ++ans;
                x = x^1;
                v[i+k-1] = 1;
            }
            x = x ^ v[i];
        }
        cout<<"Case #"<<t<<": ";
        if(ans==-1) cout<<"IMPOSSIBLE\n";
        else cout<<ans<<endl;
    }
    return 0;
}
