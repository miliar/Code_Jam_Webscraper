#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define PB push_back
#define MP make_pair

const int INF = 0x3f3f3f3f;
const int mod = 1e9 + 7;
const double eps = 1e-8;
const int maxn = 1e5+5;

int c,r,m;
char s[50][50];
int id[50][50];
int sx[15],sy[15];
int tx[15],ty[15];
int sn,tn;
int dp[1025][1025];
int idp[1025][1025];
vector<int>bit[1025];

void init(){
	for(int i=0;i<1024;++i){
		for(int j=0;j<10;++j){
			if((i&(1<<j)))bit[i].PB(j);
		}
	}
}



int main(){
	init();
	int T;
	scanf("%d",&T);
	for(int q=1;q<=T;++q){
		sn=0,tn=0;
		scanf("%d%d%d",&c,&r,&m);
		memset(id,-1,sizeof(id));
		for(int i=1;i<=c;++i)scanf("%s",s[i]+1);
		for(int i=1;i<=c;++i){
			for(int j=1;j<=r;++j){
				if(s[i][j]=='S'){
					id[i][j]=sn++;
					sx[sn]=i,sy[sn]=j;
				}
				if(s[i][j]=='T'){
					id[i][j]=tn++;
					tx[tn]=i,ty[tn]=j;
				}
			}
		}
		memset(dp,-1,sizeof(dp));
		dp[(1<<sn)-1][(1<<tn)-1]=0;
		for(int i=(1<<sn)-1;i>=0;--i){
			for(int j=(1<<tn)-1;j>=0;--j){
				if(dp[i][j]==-1)continue;
				for(int k=0;k<bit[i].size();++k){
					for(int p=0;p<bit[j].size();++p){
						int u=bit[i][k];
						int v=bit[j][p];
						if(dp[i-(1<<u)][j-(1<<v)]!=-1)continue;
						if(check(i,j,u,v)){
							dp[i-(1<<u)][j-(1<<v)]=dp[i][j]+1;
							if(dp[i][j]+1>ans)
						}
					}
				}
			}
		}

	}
	return 0;
}
