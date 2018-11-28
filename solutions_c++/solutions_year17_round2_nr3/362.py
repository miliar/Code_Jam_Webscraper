#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
#include <cstring>
#include <set>
#include <map>
using namespace std;

int N,Q;
long long E[111];
int S[111];
long long path[111][111];
double timepath[111][111];

void solve(){
	scanf("%d%d",&N,&Q);
	for (int i=0;i<N;i++){
		scanf("%lld%d",&E[i],&S[i]);
	}

	for (int i=0;i<N;i++)
		for (int j=0;j<N;j++)
			scanf("%lld",&path[i][j]);

	//step 1
	for (int k=0;k<N;k++)
		for (int i=0;i<N;i++)
			for (int j=0;j<N;j++)
			{
				if (path[i][k] == -1 || path[k][j] == -1)
					continue;
				if (path[i][j] == -1)
					path[i][j] = path[i][k] + path[k][j];
				path[i][j] = min(path[i][j] , path[i][k] + path[k][j]);
			}

	//step2
	for (int i=0;i<N;i++)
		for (int j=0;j<N;j++){
			if (path[i][j] == -1 || path[i][j] > E[i])
				timepath[i][j] = -1.0;
			else
				timepath[i][j] = (double) path[i][j] / (double)S[i];
		}

	for (int k=0;k<N;k++)
		for (int i=0;i<N;i++)
			for (int j=0;j<N;j++)
			{
				if (timepath[i][k] < -0.5 || timepath[k][j] < -0.5)
					continue;
				if (timepath[i][j] == -1)
					timepath[i][j] = timepath[i][k] + timepath[k][j];
				timepath[i][j] = min(timepath[i][j] , timepath[i][k] + timepath[k][j]);
			}


	for (int i=0;i<Q;i++){
		if (i > 0)printf(" ");
		int a,b;
		scanf("%d%d",&a,&b);
		printf("%.9lf",timepath[a-1][b-1]);
	}
	printf("\n");
}

int main(){
	int T;
	scanf("%d",&T);
	for (int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		solve();
	}
}