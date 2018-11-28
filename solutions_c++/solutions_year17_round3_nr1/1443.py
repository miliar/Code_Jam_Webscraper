#include <bits/stdc++.h>

#define LOCAL 1

#define lli long long int
#define llu unsigned long long int
#define ld long double
#define all(v) v.begin(),v.end()
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define si(n) scanf("%d",&n)
#define slli(n) scanf("%lld",&n);
#define ss(n) scanf("%s",n);

const long double EPS = 1e-8;
const int MOD = 1000000007ll;
const int mod1 = 1000000009ll;
const int mod2 = 1100000009ll;
int INF = (int)1e9;
lli INFINF = (lli)1e18;
int debug = 0;
long double PI = acos(-1.0);

using namespace std;

int bit_count(lli _x){lli _ret=0;while(_x){if(_x%2==1)_ret++;_x/=2;}return _ret;}
int bit(lli _mask,int _i){return (_mask&(1ll<<_i))==0?0:1;}
int add(int a,int b,int m=MOD){int x=a+b;while(x>=m)x-=m;while(x<0)x+=m;return x;}
int sub(int a,int b,int m=MOD){int x=a-b;while(x<0)x+=m;while(x>=m)x-=m;return x;}
int mul(int a,int b,int m=MOD){lli x=a*1ll*b;x%=m;while(x<0)x+=m;return (int)x;}
int ldtoint(ld x){return (int)(x+0.5);}lli ldtolli(ld x){return (lli)(x+0.5);}
int powermod(lli _a,lli _b,int _m=MOD){lli _r=1;while(_b){if(_b%2==1)_r=mul(_r,_a,_m);_b>>=1;_a=mul(_a,_a,_m);}return _r;}

template<class T1,class T2>ostream&operator<<(ostream& os,const pair<T1,T2>&p){os<<"["<<p.first<<","<<p.second<<"]";return os;}
template<class T>ostream&operator<<(ostream& os,const vector<T>&v){os << "[";bool first=true;for (T it:v){if (!first)os<<", ";first = false;os<<it;}os<<"]";return os;}
template<class T>ostream&operator<<(ostream& os,set<T>&v){os<<"[";bool first=true;for (T it:v){if(!first)os<<", ";first=false;os<<it;}os<<"]";return os;}
template<class T1,class T2>ostream&operator<<(ostream& os,map<T1,T2>&v){os<<"[";bool first=true;for(pair<T1,T2> it:v){if(!first)os<<", ";first=false;os<<"("<<it.F<<","<<it.S<<")";}os<<"]";return os;}
template<class T>void parr(T a[],int s,int e){cout<<"[";for(int i=s;i<e;i++)cout<<a[i]<<", ";cout<<a[e]<<"]\n";}

lli T,N,K;
lli R[1010],H[1010];
lli dp[1010][1010];

int main()
{
if(LOCAL){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    debug = 1;
}
    srand (time(NULL));
    //ios::sync_with_stdio(0);cin.tie(0);

    cout<<fixed<<setprecision(10);

    slli(T);
    for(lli t=1;t<=T;t++){
        slli(N);slli(K);
        vector<pair<lli,lli> > v;
        for(lli i=1;i<=N;i++) {
            slli(R[i]);slli(H[i]);
            v.pb({R[i],H[i]});
        }
        sort(all(v));
        reverse(all(v));
        for(int i=1;i<=N;i++){
            R[i] = v[i-1].F;
            H[i] = v[i-1].S;
        }

        for(int i=0;i<=N;i++)
            for(int j=0;j<=N;j++)
                dp[i][j] = 0;

        for(int i=1;i<=N;i++)
            dp[1][i] = R[i]*R[i] + 2*R[i]*H[i];
        for(int i=2;i<=N;i++)
            dp[1][i] = max(dp[1][i],dp[1][i-1]);
        for(int j=2;j<=K;j++){
            dp[j][j] = dp[j-1][j-1] + 2*R[j]*H[j];
            for(int i=j+1;i<=N;i++){
                dp[j][i] = max(dp[j-1][i-1] + 2*R[i]*H[i],dp[j][i-1]);
            }
        }
        //for(int i=1;i<=N;i++){for(int j=1;j<=N;j++)cout<<dp[i][j]<<" ";cout<<"\n";}cout<<ans<<"\n";
        lli ans = dp[K][N];
        cout<<"Case #"<<t<<": "<<((ld)ans*PI)<<"\n";
    }

    return 0;
}

