#include<bits/stdc++.h>
using namespace std;
const int inf = 1e9, N = 1440;

int a, b, sc[1505], dt[1505][1505][2];

void solve (int tc) {
	printf("Case #%d: ",tc);
	scanf("%d%d",&a,&b);
	for(int i=0;i<N;i++) sc[i] = 0;
	for(int i=1;i<=a;i++) {
		int S, E;
		scanf("%d%d",&S,&E);
		for(int i=S;i<E;i++) sc[i] = 1;
	}
	for(int i=1;i<=b;i++) {
		int S, E;
		scanf("%d%d",&S,&E);
		for(int i=S;i<E;i++) sc[i] = 2;
	}
	int ans = inf;
	if(sc[0] != 1) {
		dt[0][0][0] = 0;
		dt[0][0][1] = inf;
		dt[0][1][1] = inf;
		dt[0][1][0] = inf;
		for(int i=1;i<N;i++) {
			for(int j=0;j<=i+1;j++) {
				dt[i][j][0] = inf;
				dt[i][j][1] = inf;
			}
			for(int j=0;j<=i;j++) {
				if(sc[i] != 1) dt[i][j][0] = min(dt[i][j][0], min(dt[i-1][j][0], dt[i-1][j][1] + 1));
				if(sc[i] != 2) dt[i][j+1][1] = min(dt[i][j+1][1], min(dt[i-1][j][0] + 1, dt[i-1][j][1]));
			}
		}
		ans = min(ans, min(dt[N-1][N/2][0], dt[N-1][N/2][1]+1));
	}
	if(sc[0] != 2) {
		dt[0][0][0] = inf;
		dt[0][0][1] = inf;
		dt[0][1][1] = 0;
		dt[0][1][0] = inf;
		for(int i=1;i<N;i++) {
			for(int j=0;j<=i+1;j++) {
				dt[i][j][0] = inf;
				dt[i][j][1] = inf;
			}
			for(int j=0;j<=i;j++) {
				if(sc[i] != 1) dt[i][j][0] = min(dt[i][j][0], min(dt[i-1][j][0], dt[i-1][j][1] + 1));
				if(sc[i] != 2) dt[i][j+1][1] = min(dt[i][j+1][1], min(dt[i-1][j][0] + 1, dt[i-1][j][1]));
			}
		}
		ans = min(ans, min(dt[N-1][N/2][1], dt[N-1][N/2][0]+1));
	}
	printf("%d\n",ans);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tc;
	scanf("%d",&tc);
	for(int i=1;i<=tc;i++) solve(i);
}
