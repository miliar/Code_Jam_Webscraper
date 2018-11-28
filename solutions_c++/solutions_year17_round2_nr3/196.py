#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define X first
#define Y second

int n,q,TT;
double dis[111],spd[111];
double d0[111][111],d1[111][111];

int main(){
	freopen("3.in","r",stdin);
	freopen("3.out","w",stdout);
	scanf("%d",&TT);
	for (int T=1;T<=TT;++T){
		cin >>n >>q;
		for (int i=1;i<=n;++i)
			cin >>dis[i] >>spd[i];
		for (int i=1;i<=n;++i)
			for	(int j=1;j<=n;++j){
				cin >>d0[i][j];
				if	(d0[i][j] < 0)	d0[i][j] = 1e12;
				if	(i == j)
					d0[i][j] = 0;
			}
		for	(int k=1;k<=n;++k)
			for	(int i=1;i<=n;++i)
				for	(int j=1;j<=n;++j)
					if	(d0[i][k] + d0[k][j] < d0[i][j])
						d0[i][j] = d0[i][k] + d0[k][j];
		for	(int i=1;i<=n;++i)
			for	(int j=1;j<=n;++j)
				if	(i==j)	d1[i][j]=0;
				else if (dis[i] < d0[i][j]) d1[i][j] = 1e12;
				else d1[i][j] = d0[i][j] / spd[i];
		for	(int k=1;k<=n;++k)
			for	(int i=1;i<=n;++i)
				for	(int j=1;j<=n;++j)
					if	(d1[i][k] + d1[k][j] < d1[i][j])
						d1[i][j] = d1[i][k] + d1[k][j];
		printf("Case #%d:",T);
		while (q--){
			int s,r;
			cin >>s >>r;
			printf(" %.8f",d1[s][r]);
		}
		printf("\n");
	}
	return	0;
}

