#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int pt;
int dp[101][101][101][4], mark[101][101][101][4];

int N, P;
int S[5];

int get(int x,int y,int z, int r) {
	if(x+y+z==0)return 0;
	int&ret=dp[x][y][z][r];
	if(mark[x][y][z][r]==pt)return ret;
	mark[x][y][z][r]=pt;
	int c=(r==0);
	ret=0;
	if(x>0)
		ret=max(ret,c+ get(x-1,y,z,(r + 1) % P));
	if(y>0)
		ret=max(ret,c+ get(x,y-1,z,(r + 2) % P));
	if(z>0)
		ret=max(ret,c+ get(x,y,z-1,(r + 3) % P));
	return ret;
}

int run() {
	memset(S,0,sizeof(S));
	scanf("%d %d", &N, &P);
	for(int i=0;i<N;++i){
		int a;
		scanf("%d",&a);
		a %= P;
		S[a] ++;
	}
	//int ret=get(S[1],S[2],S[3],0);
	//cout << "ret="<<ret<<endl;
	return S[0] + get(S[1],S[2],S[3],0);
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int test;scanf("%d",&test);
	for(int no=1;no<=test;++no)
	{
		pt = no;
		printf("Case #%d: %d\n", no, run());
	}
}
/*
3
4 3
4 5 6 4
4 2
4 5 6 4
3 3
1 1 1
*/
