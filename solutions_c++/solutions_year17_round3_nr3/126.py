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

int n, k;
double u;
double p[50];

void solve(){
    cin >> n >> k;
    cin >> u;
    rep(i,n) cin >> p[i];
    sort(p,p+n);
    double st = 0.0, en = 1.0, mid;
    for(int i = 0; i < 1000; i++){
        mid = (st+en)/2.0;
        double sum = 0.0;
        rep(j,n){
            if(p[j] > mid) continue;
            sum += mid-p[j];
        }
        if(sum > u){
            en = mid;
        } else{
            st = mid;
        }
    }
    double ans = 1.0;
    rep(i,n){
        if(p[i] > st) ans *= p[i];
        else ans *= st;
    }
    printf("%.9f\n",ans);
}

int main(){
    int T;
    cin >> T;
    rep(i,T){
        cout << "Case #" << i+1 << ": ";
        solve();
    }
}
