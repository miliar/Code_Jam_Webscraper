#include <bits/stdc++.h>
using namespace std;
#define LL long long

LL d[105][105];
int n,q;
int tc;
LL E[105];
double S[105];
double f[105][105];
int U[105], V[105];

int main(){
	freopen("out.txt","w",stdout);
	scanf("%d",&tc);
	for ( int t = 1; t <= tc; t++ ){
		scanf("%d%d",&n,&q);
		for ( int i = 0; i < n; i++ ){
			scanf("%lld %lf",&E[i], &S[i]);
		}
		for ( int i = 0; i < n; i++ ){
			for ( int j =0 ; j < n; j++ ){
				scanf("%lld",&d[i][j]);
				if ( i == j ) d[i][j] = 0;
				
				if ( i == j ) f[i][j] = 0;
				else f[i][j] = 1e12;
				
				if ( d[i][j] == -1 ) d[i][j] = 1e12;
			}
		}
		
		for ( int k = 0; k < n; k++ ){
			for ( int i = 0; i < n; i++ ){
				for ( int j = 0; j < n; j++ ){
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
				}
			}
		}
		
		/*
		for ( int i = 0; i < n; i++ ){
			for ( int j = 0; j < n; j++ ){
				printf("%lld ",d[i][j]);
			}
			cout << endl;
		}
		//*/
		
		for ( int i = 0; i < n; i++ ){
			for ( int j =0 ; j < n; j++ ){
				if ( i == j ) continue;
				if ( d[i][j] <= E[i] ) f[i][j] = d[i][j]/S[i];
				else f[i][j] = 1e12;
			}
		}
		
		for ( int k = 0; k < n; k++ ){
			for ( int i = 0; i < n; i++ ){
				for ( int j = 0; j < n; j++ ){
					f[i][j] = min(f[i][j], f[i][k] + f[k][j]);
				}
			}
		}
		
		/*
		for ( int i = 0; i < n; i++ ){
			for ( int j = 0; j < n; j++ ){
				printf("%.9lf ",f[i][j]);
			}
			cout << endl;
		}
		//*/
		
		for ( int i = 0; i < q; i++ ){
			scanf("%d%d",&U[i],&V[i]);
			U[i]--;
			V[i]--;
		}
		
		printf("Case #%d:",t);
		for ( int i = 0; i < q; i++ ){
			int u,v;
			u = U[i], v = V[i];
			printf(" %.9lf",f[u][v]);
		}
		puts("");
	}
	fclose(stdout);
	return 0;
}
