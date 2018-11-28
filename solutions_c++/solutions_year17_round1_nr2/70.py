/*
Date: 2017/04/15 09:15:16 Saturday
*/
#include<bits/stdc++.h>
using namespace std;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define rep(i,a,n) for(int i=(a);i<=(n);++i)
#define dep(i,a,n) for(int i=(a);i>=(n);--i)
#define eps 1e-10
#define pi 3.1415926535897
#define sqr(x) ((x)*(x))
#define MAX(a,b) a=max(a,b)
#define MIN(a,b) a=min(a,b)
#define SZ(x) ((int)(x).size())
#define CPY(a,b) memcpy(a,b,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define POSIN(x,y) (1<=(x)&&(x)<=n&&1<=(y)&&(y)<=m)
#define all(x) (x).begin(),(x).end()
#define COUT(S,x) cout<<fixed<<setprecision(x)<<S<<endl
#define buli(x) (__builtin_popcountll(x))
#define bur0(x) (__builtin_ctzll(x))
#define bul2(x) (63-__builtin_clzll(x))
#define pw(x) ((ll(1))<<(x))
#define upmo(a,b) (((a)=((a)+(b))%mo)<0?(a)+=mo:(a))
#define mmo(a,b) (((a)=1ll*(a)*(b)%mo)<0?(a)+=mo:(a))
#define y0 y0z
#define y1 y1z
#define yn ynz
#define j0 j0z
#define j1 j1z
#define jn jnz
#define tm tmz
#ifdef LOCAL
#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
#define debug(...) 
#endif
typedef long long ll;
typedef double lf;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<lf,lf> pff;
typedef complex<double> CD;
const int inf=0x3f3f3f3f;
const int mo=1000000007;
inline void gn(long long&x){
	int sg=1;char c;while(((c=getchar())<'0'||c>'9')&&c!='-');c=='-'?(sg=-1,x=0):(x=c-'0');
	while((c=getchar())>='0'&&c<='9')x=x*10+c-'0';x*=sg;
}
inline void gn(int&x){long long t;gn(t);x=t;}
inline void gn(unsigned long long&x){long long t;gn(t);x=t;}
inline void gn(double&x){double t;scanf("%lf",&t);x=t;}
inline void gn(long double&x){double t;scanf("%lf",&t);x=t;}
template<class T1,class T2>inline void gn(T1&r,T2&s){gn(r),gn(s);}
template<class T1,class T2,class T3>inline void gn(T1&r,T2&s,T3&t){gn(r),gn(s),gn(t);}
template<class T1,class T2,class T3,class T4>inline void gn(T1&r,T2&s,T3&t,T4&u){gn(r),gn(s),gn(t),gn(u);}
inline void gs(char *s){scanf("%s",s);}
inline void gc(char &c){while((c=getchar())>126 || c<33);}
inline void pc(char c){putchar(c);}
const int DX[]={1,0,-1,0},DY[]={0,1,0,-1};
ll powmod(ll a,ll b) {ll res=1;a%=mo;for(;b;b>>=1){if(b&1)res=res*a%mo;a=a*a%mo;}return res;}
ll powmod(ll a,ll b,ll mo) {ll res=1;a%=mo;for(;b;b>>=1){if(b&1)res=res*a%mo;a=a*a%mo;}return res;}
ll gcd(ll a,ll b) { return b?gcd(b,a%b):a;}
//*******************************************

const int N=222,M=111111;
int l,m,n,t,C;
int a[N][N],v[N],pt[N];
pii b[N][N];
pii work(int x,int y){
	int l=0,r=inf;
	while(l<r){
		int mid=l+r>>1;
		if(1.0*x*mid>y/(1.1+eps))r=mid;else l=mid+1;
	}
	int ans=l;
	l=0,r=inf;
	while(l<r){
		int mid=l+r+1>>1;
		if(1.0*x*mid<y/(0.9-eps))l=mid;else r=mid-1;
	}
	return mp(ans,l);
}
void print(pii x){printf("%d %d\n",x.X,x.Y);}
int main(){
#ifdef LOCAL
	freopen("B.in","r",stdin);freopen("B.out","w",stdout);
#endif
	//print(work(1000000,899999));
	//printf("%.9lf\n",899999/(0.9-eps));
	scanf("%d",&C);rep(_,1,C){
		printf("Case #%d: ",_);
		scanf("%d%d",&n,&m);
		rep(i,1,n)scanf("%d",&v[i]);
		rep(i,1,n){
			rep(j,1,m)scanf("%d",&a[i][j]);
			sort(a[i]+1,a[i]+1+m);
			rep(j,1,m)b[i][j]=work(v[i],a[i][j]);
			pt[i]=1;
		}
		int ans=0;
		while(1){
			int p=0;
			rep(i,1,n)MAX(p,b[i][pt[i]].X);
			int ok=1;
			rep(i,1,n)if(b[i][pt[i]].Y<p){
				ok=0;++pt[i];
			}
			if(ok){
				++ans;
				rep(i,1,n)++pt[i];
			}
			int biu=0;
			rep(i,1,n)if(pt[i]>m)biu=1;
			if(biu)break;
		}
		printf("%d\n",ans);
	}
	return 0;
}
