#include <bits/stdc++.h>

using namespace std;

int d[150][150], v[150], m[150];
double dd[150][150];

int main(){
	int t; scanf("%d", &t);
	for (int i=1; i<=t; ++i){
		printf("Case #%d: ", i);
		int n,q; scanf("%d%d", &n, &q);
		for (int j=0; j<n; ++j){
			scanf("%d%d", &m[j], &v[j]);
		}
		for (int j=0; j<n; ++j)
		for (int k=0; k<n; ++k){
			scanf("%d", &d[j][k]);
		}
		for (int j=0; j<n; ++j) d[j][j] = 0;
		
		for (int j=0; j<n; ++j)
		for (int k=0; k<n; ++k)
		for (int l=0; l<n; ++l)
		if (d[k][j] > 0 && d[j][l] > 0)
			if (d[k][l] < 0 || d[k][l] > d[k][j] + d[j][l])
			d[k][l] = d[k][j] + d[j][l];
		
		for (int j=0; j<n; ++j){
		for (int k=0; k<n; ++k){
		if (d[j][k] <= m[j]) dd[j][k] = (double)d[j][k]/v[j];
		else dd[j][k] = -1;
		//printf ("%.6f ", dd[j][k]);
	}
	}
		
		
		for (int j=0; j<n; ++j)
		for (int k=0; k<n; ++k)
		for (int l=0; l<n; ++l)
		if (dd[k][j] > 0 && dd[j][l] > 0)
			if (dd[k][l] < 0 || dd[k][l] > dd[k][j] + dd[j][l])
			dd[k][l] = dd[k][j] + dd[j][l];

		for (int j=0; j<q; ++j){
			int u,v; scanf("%d%d", &u, &v);
			printf("%.6f ", dd[u-1][v-1]);
		}
		printf("\n");
	}
}
