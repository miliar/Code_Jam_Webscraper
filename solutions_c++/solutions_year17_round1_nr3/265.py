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

ll hd, ad, hk, ak, b, d;

ll calc(ll m, ll L){
    ll H = hd;
    ll A = ak;
    ll c = 0;
    while(m){
        if(H <= A-d){
            c++;
            H = hd-A;
        }
        else{
            A -= d;
            H -= A;
            c++, m--;
        }
        if(c >= L) return L;
    }
    if(A<=0) return c;
    ll k = L-c-1;
    while((H+A-1)/A <= k){
        k -= H/A+1;
        c++;
        H = hd-A;
    }
    return c;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    rep(t,1,T+1){
        cin>>hd>>ad>>hk>>ak>>b>>d;
        ll ans = 400;
        rep(DD,0,101){
            rep(BB,0,101){
                ll Hd = hd, Ad = ad, Ak = ak, Hk = hk, D=DD,B=BB;
                ll c = 0;
                while(D){
                    if(Hd <= Ak-d){
                        c++;
                        Hd = hd-Ak;
                    }
                    else{
                        Ak -= d;
                        Hd -= Ak;
                        c++, D--;
                    }
                    if(c >= ans) break;
                }
                while(B){
                    if(Hd <= Ak){
                        c++;
                        Hd = hd-Ak;
                    }
                    else{
                        Ad += b;
                        Hd -= Ak;
                        c++, B--;
                    }
                    if(c >= ans) break;
                }
                while(Hk-Ad > 0){
                    if(Hd <= Ak){
                        c++;
                        Hd = hd-Ak;
                    }
                    else{
                        Hk -= Ad;
                        Hd -= Ak;
                        c++;
                    }
                    if(c >= ans) break;
                }
                ans = min(c+1,ans);
            }
        }
        if(ans==400) cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
