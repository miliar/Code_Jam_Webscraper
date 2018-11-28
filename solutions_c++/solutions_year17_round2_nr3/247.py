#include <bits/stdc++.h>
#define fr(x) scanf("%d", &x)
using namespace std;

double d[128][128], d2[128][128];
pair<double, double> p[128];

int main(){
	int n, q;
	int t;
	fr(t);
	for(int t1=1; t1<=t ;++t1){
		fr(n);
		fr(q);
		for(int i=1; i<=n; ++i){
			scanf("%lf%lf", &p[i].first, &p[i].second);
		}
		for(int i=1; i<=n; ++i){
			for(int j=1; j<=n; ++j){
				scanf("%lf", &d[i][j]);
			}
			d[i][i] = 0;
		}
		for(int i=1; i<=n; ++i){
			for(int j=1; j<=n; ++j){
				if(d[i][j] == -1) d[i][j] = 1e14; 
			}
		}
		for(int k=1; k<=n; ++k){
			for(int i=1; i<=n; ++i){
				for(int j=1; j<=n; ++j){
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
				}
			}
		}
		for(int i=1; i<=n; ++i){
			for(int j=1; j<=n; ++j){
				if(d[i][j] > p[i].first){
					d2[i][j] = 1e14; 
				}
				else {
					d2[i][j] = d[i][j] / p[i].second;
				}
			}
		}
		for(int k=1; k<=n; ++k){
			for(int i=1; i<=n; ++i){
				for(int j=1; j<=n; ++j){
					d2[i][j] = min(d2[i][j], d2[i][k] + d2[k][j]);
				}
			}
		}
		printf("Case #%d: ", t1);
		while(q--){
			int a, b; 
			fr(a);
			fr(b);
			printf("%.7lf ", d2[a][b]);
		}
		puts("");
	}	
}