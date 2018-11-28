#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define X first
#define Y second
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define FILL(a,x) memset(a,x,sizeof(a))
#define	foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define	mp make_pair
#define	pb push_back
#define sz(a) int((a).size())
#define all(a)  a.begin(), a.end()
#define	debug(ccc)	cout << #ccc << " = " << ccc << endl;
#define present(c,x) ((c).find(x) != (c).end())
const double eps = 1e-8;
#define EQ(a,b) (fabs((a)-(b))<eps)
inline int max(int a,int b){return a<b?b:a;}
inline int min(int a,int b){return a>b?b:a;}
inline ll max(ll a,ll b){return a<b?b:a;}
inline ll min(ll a,ll b){return a>b?b:a;}
const int mod = 1e9+7;
const int N = 1e6+10;
const ll inf = 1e18;

ll power(ll a,ll n){
	if(n==0){
		return 1;
	}
	ll b = power(a,n/2);
	b = b*b%mod;
	if(n%2) b= b*a%mod;
	return b;
}

int add(int a,int b){ return (a+b)%mod;}
int mul(int a,int b){ return (ll)a*b%mod;}


int dp3[101][101][4],dp4[101][101][101][4];

int f3(int a,int b,int l){
	if(a+b==0) return 0;
	int &ret = dp3[a][b][l];
	if(ret!=-1) return ret;
	ret = 0;
	if(a){
		ret = max(ret, f3(a-1,b,(l-1+3)%3) + (l==0));
	}
	if(b) 
		ret = max(ret, f3(a,b-1,(l-2+3)%3) + (l==0));
	return ret;
}


int f4(int a,int b,int c,int l){
	if(a+b+c==0) return 0;
	int &ret = dp4[a][b][c][l];
	if(ret!=-1) return ret;
	ret = 0;
	if(a){
		ret = max(ret, f4(a-1,b,c,(l-1+4)%4) + (l==0));
	}
	if(b) 
		ret = max(ret, f4(a,b-1,c,(l-2+4)%4) + (l==0));
	if(c)
		ret = max(ret, f4(a,b,c-1,(l-3+4)%4) + (l==0));
	return ret;
}

int main(){
 // 	freopen("nice.in","r",stdin);
 // freopen("nice.out","w",stdout);
	int t;
	scanf("%d",&t);
	FILL(dp3,-1); FILL(dp4,-1);
	REP(tt,t){
		int n,p; scanf("%d %d",&n,&p); 
		int ar[4]={0};
		REP(i,n){
			int x; scanf("%d",&x);
			ar[x%p]++;
		}
		int ans = 0;
		if(p==2){
			ans = ar[0] + (ar[1]+1)/2; 
		}else if(p==3){
			ans = ar[0] + f3(ar[1],ar[2],0);
			// printf("gg%d %d\n",ans,ar[0]);
		}else ans = ar[0] + f4(ar[1],ar[2],ar[3],0);
		printf("Case #%d: %d\n",tt+1,ans);
	}
	return 0;
}


	