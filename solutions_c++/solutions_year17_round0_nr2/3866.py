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


vector < int > A,B;

int main(){
 // 	freopen("nice.in","r",stdin);
 // freopen("nice.out","w",stdout);
	int t; scanf("%d",&t);
	REP(tt,t){
		ll n; scanf("%lld",&n);
		A.clear(); B.clear();
		// int ans = 1;
		// REPP(i,1,n+1){
		// 	int x = i;
		// 	A.clear();
		// 	while(x) A.pb(x%10),x/=10;
		// 	int f = 1;
		// 	REP(j,(int)A.size()-1) if(A[j]<A[j+1]) f=0;
		// 	if(f) ans = i;
		// }
		// printf("Case #%d: %d\n",tt+1,ans);continue;
		while(n){
			A.pb(n%10); n/=10;
		}
		int f = 0;
		while(A.size()){
			if(f){
				B.pb(9);A.pop_back();continue;
			}
			int g = 0;
			for(int j = (int)A.size()-1;j>=0;j--){
				if(A[j]>A.back()){
					g=1;B.pb(A.back()),A.pop_back(); break;	
				}else if(A[j]<A.back()){
					g=1; f=1; B.pb(A.back()-1); A.pop_back(); break;
				}
			}
			if(!g) B.pb(A.back()),A.pop_back();
			// REP(i,(int)A.size()-1) if(A[i]==0){
			// 	g = 1; f=1; B.pb(A.back()-1); A.pop_back(); break;
			// }
		}
		reverse(all(B));
		while(B.size() && B.back()==0) B.pop_back();
		reverse(all(B));
		printf("Case #%d: ",tt+1);
		REP(i,B.size()) printf("%d",B[i]);printf("\n");
	}
	return 0;
}


