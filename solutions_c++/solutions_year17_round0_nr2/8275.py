#include<bits/stdc++.h>
using namespace std;
#define INF 0x3f3f3f3f
#define DINF 1e10
#define EPS 1e-15
#define PII acos(-1)
#define LL long long
#define Pii pair<int,int>
#define For(i,n) for(int i=0;i<n;i++)
#define ileer(n) scanf("%d",&n)
#define i2leer(n,m) scanf("%d %d",&n,&m)
#define fleer(n) scanf("%lf",&n)
#define f2leer(n,m) scanf("%Lf %Lf",&n,&m)
#define MK make_pair
#define PB push_back
#define llenar(arr,val) memset(arr,val,sizeof(arr))
#define VLL vector< LL >
#define matrix vector<VI >
#define F first
#define S second
#define MAXN 1005





int main(){

	int t;
	ileer(t);
	For(c,t){
		string g;
		cin>>g;
		int n=g.size();

			for(int i=n-2;i>=0;i--){
				if(g[i]>g[i+1]){
					for(int j=i+1;j<n;j++){
						g[j]='9';
					}
					int k=i;
					g[k]-=1;
					while(k>0 && g[k]=='0'){
						g[k]='9';
						if(k-1>=0){
							g[k-1]-=1;
						}
						k--;
					}
					
				}
			}
		string res="";
		int i=0;
		while(g[i]=='0' && i<n){
			i++;
		}
		res=g.substr(i,g.size());
		
		
		
		printf("Case #%d: %s\n",c+1,res.c_str());
	}
}