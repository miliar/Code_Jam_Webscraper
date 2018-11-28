#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<deque>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<stdlib.h>
#include<cassert>
using namespace std;
const long long mod=1000000007;
const long long inf=mod*mod;
const long long d2=500000004;
const double EPS=1e-10;
const double PI=acos(-1.0);
int ABS(int a){return max(a,-a);}
long long ABS(long long a){return max(a,-a);}
char in[60][60];
int g[1<<10][10][10];
int bfs[60][60];
vector<int>fi[60][60];
int sr[10];
int sc[10];
int tr[10];
int tc[10];
int dp[1<<10][1<<10];
int rev[1<<10][1<<10][2];
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

int ra[20];
int rb[20];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a,b,c;
		scanf("%d%d%d",&b,&a,&c);
		for(int i=0;i<a;i++)scanf("%s",in[i]);
		printf("Case #%d: ",t);
		int sn=0;
		int tn=0;
		for(int i=0;i<a;i++)for(int j=0;j<b;j++){
			if(in[i][j]=='S'){
				sr[sn]=i;sc[sn++]=j;
			}
			if(in[i][j]=='T'){
				tr[tn]=i;tc[tn++]=j;
			}
		}
		for(int i=0;i<(1<<10);i++)for(int j=0;j<10;j++)for(int k=0;k<10;k++)g[i][j][k]=0;
		for(int i=0;i<(1<<tn);i++){
			for(int j=0;j<a;j++)for(int k=0;k<b;k++){
				fi[j][k].clear();
			}
			for(int j=0;j<tn;j++){
				if(!(i&(1<<j)))continue;
				int row,col;
				row=tr[j];
				col=tc[j];
				while(row>=0){
					if(in[row][col]=='#')break;
					fi[row][col].push_back(j);
					row--;
				}
				row=tr[j];
				col=tc[j];
				while(col>=0){
					if(in[row][col]=='#')break;
					fi[row][col].push_back(j);
					col--;
				}
				row=tr[j];
				col=tc[j];
				while(row<a){
					if(in[row][col]=='#')break;
					fi[row][col].push_back(j);
					row++;
				}
				row=tr[j];
				col=tc[j];
				while(col<b){
					if(in[row][col]=='#')break;
					fi[row][col].push_back(j);
					col++;
				}
			}
			for(int j=0;j<sn;j++){
				for(int k=0;k<a;k++)for(int l=0;l<b;l++)bfs[k][l]=-1;
				bfs[sr[j]][sc[j]]=0;
				queue<pair<int,int> > Q;
				Q.push(make_pair(sr[j],sc[j]));
				while(Q.size()){
					int row=Q.front().first;
					int col=Q.front().second;
					Q.pop();
					if(fi[row][col].size()){
						for(int k=0;k<fi[row][col].size();k++){
			//				if(i==(1<<tn)-1)printf("%d %d %d\n",i,j,fi[row][col][k]);
							g[i][j][fi[row][col][k]]=1;
						}
						continue;
					}
					if(bfs[row][col]==c)continue;
					
					for(int k=0;k<4;k++){
						int tor=row+dx[k];
						int toc=col+dy[k];
						if(tor<0||toc<0||tor>=a||toc>=b)continue;
						bool dame=false;
						for(int l=0;l<tn;l++)if((i&(1<<tn))&&tor==tr[l]&&toc==tc[l])dame=true;
						if(in[tor][toc]=='#')continue;
						if(dame){
							continue;
						}
						if(!~bfs[tor][toc]){
							bfs[tor][toc]=bfs[row][col]+1;
							Q.push(make_pair(tor,toc));
						}
					}
				}
			}
		}
		for(int i=0;i<(1<<sn);i++)for(int j=0;j<(1<<tn);j++){
			dp[i][j]=-mod;
		}
		dp[0][0]=0;
		int ret=0;
		int ar=0;
		int ac=0;
		for(int i=0;i<(1<<sn);i++){
			for(int j=0;j<(1<<tn);j++){
				if(dp[i][j]<0)continue;
				if(ret<dp[i][j]){
					ret=dp[i][j];
					ar=i;ac=j;
				}
				for(int k=0;k<sn;k++){
					if(i&(1<<k))continue;
					for(int l=0;l<tn;l++){
						if(j&(1<<l))continue;
						if(g[(1<<tn)-1-j][k][l]){
							if(dp[i+(1<<k)][j+(1<<l)]<dp[i][j]+1){
								dp[i+(1<<k)][j+(1<<l)]=dp[i][j]+1;
								rev[i+(1<<k)][j+(1<<l)][0]=k;
								rev[i+(1<<k)][j+(1<<l)][1]=l;
								
							}
						}
					}
				}
			}
		}
		printf("%d\n",ret);
		for(int i=0;i<ret;i++){
			int A=ra[ret-1-i]=rev[ar][ac][0];
			int B=rb[ret-1-i]=rev[ar][ac][1];
			ar-=(1<<A);
			ac-=(1<<B);
		}
		for(int i=0;i<ret;i++)printf("%d %d\n",ra[i]+1,rb[i]+1);
	}
}