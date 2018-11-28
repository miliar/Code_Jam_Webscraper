#include <bits/stdc++.h>
#define F first
#define S second
#define pb push_back
#define mk make_pair
#define ll long long
using namespace std;
typedef pair<int, int> pii;
const ll MOD=1e9+7;
const int N=1e3+4;

vector< pii > v;
int par[1];
int find(int x){return x==par[x]?x:par[x]=find(par[x]);}
void join(int x, int y){par[find(x)]=y;}
ll expo(ll a,ll b,ll mod){ll ans=1; while(b){if(b&1) ans=(ans*a)%mod; a=(a*a)%mod; b>>=1;} return ans;}
int gcd(int a, int b, int& x, int& y) {if(a==0){x=0;y=1;return b;}
int x1, y1;int d=gcd(b%a, a, x1, y1);x=y1-(b/a)*x1;y=x1;return d;}

int main(){
	int test,n,d,i,k;
	double ans,t,cur,tt;
	pii a;
	scanf("%d",&test);
	for(k=0;k<test;++k){
		v.clear();
		scanf("%d%d",&d,&n);
		for(i=0;i<n;++i){
			scanf("%d%d",&a.F,&a.S);
			v.pb(a);
		}
		sort(v.begin(), v.end());
		tt=(0.0+d-v[n-1].F)/v[n-1].S;
		for(i=n-2; i>=0; --i){
			t=(0.0+d-v[i].F)/v[i].S;
			if(t>=tt)
				tt=t;
		}
		ans=d/tt;
		printf("Case #%d: %.6lf\n", k+1, ans);
	}
	return 0;
}