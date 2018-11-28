#include <bits/stdc++.h>

//LIFE IS NOT A PROBLEM TO BE SOLVED

using namespace std;

#define rep(i,a,b) for(int i = int(a); i < int(b) ; i++)
#define pb push_back
#define mp make_pair
#define F first
#define S second

typedef long long int ll;
typedef unsigned long long int ull;
typedef pair < double, double > ii;
typedef pair < ll, ii > iii;

const int INF = 0x3f3f3f3f;
const ll LINF = 1LL<<52;

int main(){

	
	int T; cin >> T;
	
	rep(z, 1, T+1){
		
		double mat[111][111], time[111][111];
		double ds[111], vel[111];
		
		int N, Q; cin >> N >> Q;
		
		rep(i, 1, N+1) cin >> ds[i] >> vel[i];
		
		rep(i, 1, N+1){
			rep(j, 1, N+1){
				cin >> mat[i][j];
				if(mat[i][j]<0) mat[i][j]=LINF;
				time[i][j]=LINF;
			}
			time[i][i]=mat[i][i]=0.0;
		}		
		
		rep(k, 1, N+1)
		rep(i, 1, N+1)
		rep(j, 1, N+1){
			double aux=mat[i][k]+mat[k][j];
			if(aux>ds[i]) continue;
			mat[i][j]=min(mat[i][j], aux);
		}
		
		rep(i, 1, N+1){
			rep(j, 1, N+1){
				if(mat[i][j]>=LINF-2) continue;
				time[i][j]=mat[i][j]/vel[i];
			}
		}
		
		rep(k, 1, N+1)
		rep(i, 1, N+1)
		rep(j, 1, N+1){
			time[i][j]=min(time[i][j], time[i][k]+time[k][j]);
		}
		
		int u, v;
		printf("Case #%d:", z);
		while(Q--){
			scanf("%d %d", &u, &v);
			printf(" %.8lf", time[u][v]);
		}	printf("\n");
		
	}

	return 0;
	
}
