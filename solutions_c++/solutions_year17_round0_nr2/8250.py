#include <bits/stdc++.h>
#define rep(i,n) for(int i = 0; i < n; i++)
#define rep1(i,n) for(int i = 1; i < n; i++)
#define repv(i,n) for(int i = n-1; i >= 0; i--)
#define fi first
#define sc second
#define pb push_back
using namespace std;
typedef long long ll;

char BUF[3500000];
inline void I(int&a){scanf("%d",&a);}
inline void I(int&a,int&b){scanf("%d%d",&a,&b);}
inline void I(int&a,int&b,int&c){scanf("%d%d%d",&a,&b,&c);}
inline void I(int&a,int&b,int&c,int&d){scanf("%d%d%d%d",&a,&b,&c,&d);}
inline void L(ll&a){scanf("%lld",&a);}
inline void L(ll&a,ll&b){scanf("%lld%lld",&a,&b);}
inline void L(ll&a,ll&b,ll&c){scanf("%lld%lld%lld",&a,&b,&c);}
inline void L(ll&a,ll&b,ll&c,ll&d){scanf("%lld%lld%lld%lld",&a,&b,&c,&d);}
inline void S(string&str){str.clear();scanf("%s",BUF);int s=strlen(BUF);rep(i,s)str.pb(BUF[i]);}
inline void SV(vector<int>&v){v.clear();scanf("%s",BUF);int s=strlen(BUF);rep(i,s)if('a'<=BUF[i]&&BUF[i]<='z')v.pb(BUF[i]-'a');else v.pb(BUF[i]-'A');}

const auto EPS = 1e-10;
const auto INF = 100000000;
const auto MOD = 1000000007;
typedef pair<ll,ll> P;

void solve(){
    ll n;
    vector<int> d;
    cin >> n;
    int keta = 0;
    {
        ll N = n;
        while(N){
            d.push_back(N%10);
            keta++;
            N /= 10;
        }
        reverse(d.begin(),d.end());
    }
    if(keta == 1){
        cout << n << endl;
        return;
    }
    ll piv = 0;
    rep(i,keta) piv = piv*10+1;
    if(piv > n){
        piv = 0;
        rep(i,keta-1) piv = piv*10+9;
        cout << piv << endl;
        return;
    }
    ll ans = 0;
    rep(i,keta){
        piv = ans;
        for(int j = i; j < keta; j++) piv = piv*10+d[i];
        if(piv <= n) ans = ans*10+d[i];
        else{
            ans = ans*10+d[i]-1;
            for(int j = i+1; j < keta; j++) ans = ans*10+9;
            cout << ans << endl;
            return;
        }
    }
    cout << ans << endl;
}

int main(){
    int T;
    I(T);
    for(int i = 1; i <= T; i++){
        cout << "Case #" << i << ": ";
        solve();
    }
}






























