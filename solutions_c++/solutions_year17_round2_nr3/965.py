#include<bits/stdc++.h>
using namespace std;
#define ALL(v) (v).begin(),(v).end()
int main() {
	int T; cin >> T;
	for(int tc=1;tc<=T;tc++) {
		int n, q; cin >> n >> q;
		static int E[101],S[101];
		for(int i=1;i<=n;i++)cin>>E[i]>>S[i];
		static long long D[101][101];
		for(int i=1;i<=n;i++)for(int j=1;j<=n;j++){ cin>>D[i][j]; if (D[i][j]==-1)D[i][j]=1e18; }
		for(int k=1;k<=n;k++)for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)D[i][j]=min(D[i][j],D[i][k]+D[k][j]);
		static long double T[101][101];
		for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)T[i][j]=1e18;
		for(int i=1;i<=n;i++)for(int j=1;j<=n;j++){
			if(D[i][j] <= E[i]){
				T[i][j] = (long double) D[i][j] / (long double) S[i];
			}
		}
		for(int k=1;k<=n;k++)for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)T[i][j]=min(T[i][j],T[i][k]+T[k][j]);
		printf("Case #%d:",tc);for(int it=0;it<q;it++){int u,v;cin>>u>>v;printf(" %.9Lf",T[u][v]);}
		printf("\n");
	}
}
