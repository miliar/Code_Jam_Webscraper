#include<bits/stdc++.h>
#define lp(i,l,r)for(int i=l;i<=r;++i)
#define rp(i,r,l)for(int i=r;i>=l;--i)
#define lv(i,a)for(int i=0;i<a.size();++i)
#define rv(i,a)for(int i=(int)a.size()-1;i>=0;--i)
#define mc int T;cin>>T;lp(I,1,T)
#define pc(a)cout<<setprecision(a)<<fixed
#define io(a,b)freopen(#a,"r",stdin),\
    freopen(#b,"w",stdout)
#define al(a)a.begin(),a.end()
#define va(x,y,n,m)(x>0&&x<=n&&y>0&&y<=m)
#define vb(x,y,n,m)(x>=0&&x<n&&y>=0&&y<m)
int d4[4][2]={{-1,0},{1,0},{0,1},{0,-1}};
int d8[8][2]={{-1,0},{1,0},{0,1},{0,-1},{-1,1},{1,-1},{1,1},{-1,-1}};
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vpii;
template<class T=int>T ipt(){T a;cin>>a;return a;}
template<class T>T sqr(T a){return a*a;}
ll inf=~0u>>1,mod=1e9+7;
ll gcd(ll a,ll b){return b?gcd(b,a%b):a;}
ll lcm(ll a,ll b){return a/gcd(a,b)*b;}
ll add(ll a,ll b,ll p=mod){return (a+b)%p;}
ll sub(ll a,ll b,ll p=mod){return (a-b+p)%p;}
ll mul(ll a,ll b,ll p=mod){return a*b%p;}
ll pow(ll a,ll b,ll p=mod,ll r=1){
    b?(r=pow(a,b/2,p),r=r*r%p*(b%2?1:a)%p):0;return r;}
ll inv(ll a,ll p=mod){return pow(a,p-2);}
ll div(ll a,ll b,ll p=mod){return a*inv(b,p)%p;}
template<class T>int ckl(T&a,T b){return b<a?a=b,1:0;}
template<class T>int ckg(T&a,T b){return b>a?a=b,1:0;}
template<class T=int>vector<T>arr(int n){return vector<T>(n);}
template<class T=int>vector<vector<T>>mat(int n,int m){
    return vector<vector<T>>(n,vector<T>(m));}
template<class T>istream&operator>>(istream&s,vector<T>&a){
    if(!a.size()){int n;s>>n;a=arr<T>(n);}
    lp(i,0,a.size()-1)s>>a[i];return s;}
template<class T>istream&operator>>(istream&s,vector<vector<T>>&a){
    if(!a.size()){int n,m;s>>n>>m;a=mat<T>(n,m);}
    lp(i,0,a.size()-1)lp(j,0,a[i].size()-1)s>>a[i][j];return s;}
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;cin>>T;
    for(int I=1;I<=T;++I){
        int n,k;
        static pair<int,int>pan[1010];
        scanf("%d%d",&n,&k);
        lp(i,1,n){
            scanf("%d%d",&pan[i].first,&pan[i].second);
        }
        sort(pan+1,pan+n+1);
        reverse(pan+1,pan+n+1);
        static long double dp[1010][1010];
        lp(i,1,n){
            lp(j,1,n){
                if(j>i)
                    dp[i][j]=-1e100;
                else{
                    long double t1=dp[i-1][j];
                    long double t2=dp[i-1][j-1]+2*acos((long double)(-1.0))*pan[i].first*pan[i].second;
                    if(j-1==0)
                        t2+=acos(-1.0)*pan[i].first*pan[i].first;
                    dp[i][j]=max(t1,t2);
                }
               // if(dp[i][j]>-1e50)
                  //  cout<<i<<" "<<j<<" "<<dp[i][j]<<endl;
            }
        }
        long double ans=dp[n][k];

        cout<<setprecision(12)<<fixed;
        cout<<"Case #"<<I<<": "<<ans<<endl;
    }
    return 0;
}
