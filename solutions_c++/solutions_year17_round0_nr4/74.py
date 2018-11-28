#include<stdio.h>
#include<memory.h>
#include<stdlib.h>

int N, M, mp[111][111], nmp[111][111];
int ho[111], ve[111], grp[444][444], chk[444]; // 0 : source, 1~(2N-1) : (x+y-1), 2N~(4N-2) : (x-y+3N-1), 4N-1 : sink
int hc, vc, nh[111], nv[111];

int dfs(int ix){
	if(ix == 4*N-1)return 1;
	chk[ix]=1;
	for(int e=4*N; e--;){
		if(chk[e] || grp[ix][e]==0)continue;
		if(dfs(e)){
			grp[ix][e]=0, grp[e][ix]=1;
			return 1;
		}
	}
	return 0;
}

void test(int tn){
	scanf("%d%d", &N, &M);
	memset(mp, 0, sizeof(mp)), memset(ho, 0, sizeof(ho)), memset(ve, 0, sizeof(ve));
	memset(grp, 0, sizeof(grp));
	while(M--){
		char typ; int x, y;
		scanf("\n%c %d%d", &typ, &x, &y);
		if(typ == '+') mp[x][y] = 1; // bishop
		if(typ == 'x') mp[x][y] = 2; // rook
		if(typ == 'o') mp[x][y] = 3; // bishop + rook
	}
	memcpy(nmp, mp, sizeof(nmp));

	for(int i=1; i<=2*N-1; i++)grp[0][i] = grp[2*N-1+i][4*N-1] = 1;
	for(int i=1; i<=N; i++){
		for(int j=1; j<=N; j++){
			grp[i+j-1][i-j+3*N-1] = 1;
			if(mp[i][j]&2) ho[i]=ve[j]=1;
			if(mp[i][j]&1) grp[0][i+j-1] = grp[i-j+3*N-1][4*N-1] = 0;
		}
	}
	hc=vc=0;
	for(int i=1; i<=N; i++){
		if(!ho[i])nh[hc++]=i;
		if(!ve[i])nv[vc++]=i;
	}
	for(int i=0; i<hc; i++)nmp[nh[i]][nv[i]] |= 2;
	while(1){
		memset(chk, 0, sizeof(chk));
		if(!dfs(0))break;
	}
	int sco=0, dif=0; char tab[5]=".+xo";
	for(int i=1; i<=N; i++){
		for(int j=1; j<=N; j++){
			if(grp[i-j+3*N-1][i+j-1] == 1)nmp[i][j] |= 1;
			if(nmp[i][j]&1)sco++;
			if(nmp[i][j]&2)sco++;
			if(nmp[i][j] != mp[i][j])dif++;
		}
	}
	printf("Case #%d: %d %d\n", tn, sco, dif);
	for(int i=1; i<=N; i++){
		for(int j=1; j<=N; j++){
			if(nmp[i][j] != mp[i][j])printf("%c %d %d\n", tab[nmp[i][j]], i, j);
		}
	}
}

int main(){
	int t;
	freopen("D-large.in", "r", stdin), freopen("output.txt","w",stdout);
	scanf("%d", &t);
	for(int i=1; i<=t; i++)test(i);
	return 0;
}
