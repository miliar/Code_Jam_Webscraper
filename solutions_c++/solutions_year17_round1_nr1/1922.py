#include <bits/stdc++.h>
#define F first
#define S second
#define pb push_back
#define mk make_pair
#define ll long long
using namespace std;
typedef pair<int, int> pii;
const ll MOD=1e9+7;
const int N=30;

int par[1];
int find(int x){return x==par[x]?x:par[x]=find(par[x]);}
void join(int x, int y){par[find(x)]=y;}
ll expo(ll a,ll b,ll mod){ll ans=1; while(b){if(b&1) ans=(ans*a)%mod; a=(a*a)%mod; b>>=1;} return ans;}
int gcd(int a, int b, int& x, int& y) {if(a==0){x=0;y=1;return b;}int x1, y1;int d=gcd(b%a, a, x1, y1);x=y1-(b/a)*x1;y=x1;return d;}

char res[N][N], s[N];

int main(){
	int test,n,m,i,j,k;
	char cur;
	scanf("%d",&test);
	for(k=0;k<test;++k){
		memset(res, 0, sizeof(res));
		scanf("%d%d",&n,&m);
		for(i=0;i<n;++i){
			scanf(" %s",s);
			cur='?';
			for(j=0;j<m;++j){
				if(s[j]!='?')
					cur=s[j];
				res[i][j]=cur;
			}
			if(cur!='?'){
				for(j=m-1;j>=0 && res[i][j]!='?';--j);
				cur=res[i][j+1];
				for(;j>=0;--j)
					res[i][j]=cur;
			}
			else{
				if(i>0){
					for(j=0;j<m;++j)
						res[i][j]=res[i-1][j];
				}
			}
		}
		for(i=n-1; i>=0; --i){
			for(j=0; j<m && res[i][j]=='?'; ++j);
			if(j==m){
				for(j=0;j<m;++j)
					res[i][j]=res[i+1][j];
			}
		}
		printf("Case #%d: \n", k+1);
		for(i=0;i<n;++i){
			for(j=0;j<m;++j)
				printf("%c", res[i][j]);
			printf("\n");
		}
	}
	return 0;
}