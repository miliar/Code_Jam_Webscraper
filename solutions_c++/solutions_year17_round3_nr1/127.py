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
const double PI = 3.1415926535897932384626433832795028841971;
typedef pair<double,double> P;

int n, k;
P x[1000];
double v[1000];


void solve(){
    cin >> n >> k;
    rep(i,n) cin >> x[i].first >> x[i].second;
    sort(x,x+n,greater<P>());
    rep(i,n){
        v[i] = x[i].first*PI*2*x[i].second;
    }
    double ans = 0.0;
    for(int i = 0; i < n; i++){
        if(i+k > n) break;
        vector<double> tmp;
        double cnt = v[i];
        cnt += x[i].first*x[i].first*PI;
        for(int j = i+1; j < n; j++){
            tmp.push_back(v[j]);
        }
        sort(tmp.begin(), tmp.end(), greater<double>());
        rep(j,k-1) cnt += tmp[j];
        ans = max(ans,cnt);
    }
    printf("%.9f\n", ans);
}

int main(){
    int T;
    cin >> T;
    rep(i,T){
        cout << "Case #" << i+1 << ": ";
        solve();
    }
}
