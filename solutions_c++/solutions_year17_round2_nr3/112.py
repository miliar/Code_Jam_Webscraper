#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
#define ii pair<int,int>
#define vii vector<pair<int,int> >
#define vi vector<int>

double dist[110][110] , ti[110][110] ;
pair<double , double> arr[110] ;
int n , q ;

int main(){
    freopen("C_large.in","r",stdin);
    freopen("C_large.out","w",stdout);
	int t;
	int x , y ;
	double a ;
	scanf("%d",&t) ;
	for(int T = 1 ;T<=t;T++){
		scanf("%d%d",&n,&q) ;
		for(int i=1;i<=n;i++) scanf("%lf%lf" , &arr[i].fi , &arr[i].se) ;
		for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) scanf("%lf",dist[i]+j ) ;
		for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) dist[i][j] = ( (i==j) ? 0 : ( (dist[i][j] == -1) ? 1e18 : dist[i][j] ) );
		for(int k=1;k<=n;k++) for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) dist[i][j] = min(dist[i][j] , dist[i][k] + dist[k][j] ) ;
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				if(dist[i][j] > arr[i].fi) ti[i][j] = 1e18 ;
				else ti[i][j] = dist[i][j] / arr[i].se ;
			}
		}
		for(int k=1;k<=n;k++) for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) ti[i][j] = min(ti[i][j] , ti[i][k] + ti[k][j] ) ;
		printf("Case #%d:",T) ;
		for(int i=0;i<q;i++){
			scanf("%d%d",&x,&y) ;
			printf(" %.7lf",ti[x][y]) ;
		}
		printf("\n");
	}
	return 0;
}
