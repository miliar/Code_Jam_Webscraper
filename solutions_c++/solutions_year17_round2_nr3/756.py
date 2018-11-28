#include <bits/stdc++.h>

using namespace std;

#define INTMAX 0x7FFFFFFF
#define INTMIN -0x80000000
#define LONGMAX 0x7FFFFFFFFFFFFFFF
#define LONGMIN -0x8000000000000000


int main(){
	int T;
	cin>>T;
	for(int tc=1; tc<=T; tc++){
		int n,q;
		cin>>n>>q;
		
		long long d[n+1][n+1];
		int e[n+1];
		int s[n+1];
		
		for(int i=1; i<=n; i++){
			cin>>e[i]>>s[i];
		}
		
		for(int i=1; i<=n; i++){
			for(int j=1; j<=n; j++){
				cin>>d[i][j];
				if(d[i][j]==-1)
					d[i][j] = LONGMAX;
			}
		}
		
		//calculate shortest distances
		for (int k = 1; k <= n; k++) {
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					if(d[i][k]==LONGMAX || d[k][j]==LONGMAX)
						continue;
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
				}
			}
		}

		//transform distance to travel time
		double t[n+1][n+1];
		for(int i=1; i<=n; i++){
			for(int j=1; j<=n; j++){
				if(d[i][j]==LONGMAX || d[i][j]>e[i])
					t[i][j] = 1e16;
				else
					t[i][j] = ((double)d[i][j])/((double)s[i]);
			}
		}
		
		//calculate shortest travel time
		for (int k = 1; k <= n; k++) {
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					if(t[i][k]>1e15 || t[k][j]>1e15)
						continue;
					t[i][j] = min(t[i][j], t[i][k] + t[k][j]);
				}
			}
		}
		
		cout.precision(10);
		cout<<"Case #"<<tc<<": ";
		for(int i=0; i<q; i++){
			int u,v;
			cin>>u>>v;
			cout<<fixed<<t[u][v]<<" ";
		}
		cout<<endl;
		
	}
}