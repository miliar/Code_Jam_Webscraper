#include <bits/stdc++.h>
#define M 100
using namespace std;

char d[4][M+1][M+1][M+1][M+1];

char process(int g,int x,int y,int z,int w){
	if(~d[g][x][y][z][w]) return d[g][x][y][z][w]+((y+2*z+3*w)%(g+1)==0);
	if(x) d[g][x][y][z][w]=max(d[g][x][y][z][w],process(g,x-1,y,z,w));
	if(y) d[g][x][y][z][w]=max(d[g][x][y][z][w],process(g,x,y-1,z,w));
	if(z) d[g][x][y][z][w]=max(d[g][x][y][z][w],process(g,x,y,z-1,w));
	if(w) d[g][x][y][z][w]=max(d[g][x][y][z][w],process(g,x,y,z,w-1));
	return d[g][x][y][z][w]+((y+2*z+3*w)%(g+1)==0);
}

int main(){
	freopen("input.txt","r",stdin);

	int t,i,j,a[4];
	scanf("%d",&t);
	memset(d,-1,sizeof(d));
	for(i=1;i<4;i++) d[i][0][0][0][0]=0;
	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		int n,g,x;
		scanf("%d %d",&n,&g);
		for(j=0;j<4;j++) a[j]=0;
		for(j=1;j<=n;j++) scanf("%d",&x),a[x%g]++;
		process(g-1,a[0],a[1],a[2],a[3]);
		printf("%d\n",d[g-1][a[0]][a[1]][a[2]][a[3]]);
	}
	return 0;
}
