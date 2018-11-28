#include <cstdio>
#include <cstring>
using namespace std;
char g[30][30];
bool used[30][30];
bool check(int u, int d, int j, char ch)
{
	for(int i=u;i<=d;i++){
		if(g[i][j]!='?'&&g[i][j]!=ch){
			//printf("false %d %d %c %c\n",i,j,g[i][j],ch);
			return false;
		}
	}
	return true;
}
int main()
{
	int T;
	int r,c;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++) {
		memset(used,0,sizeof(used));
		scanf("%d%d",&r,&c);
		for(int i=0;i<r;i++){
			scanf("%s",g[i]);
		}
		//printf("%d %d\n",r,c);
		for(int j=0;j<c;j++){
			for(int i=0;i<r;i++){
				//printf("%d %d\n",i,j);
				//pintf("%d %d\n",r,c);
				if(g[i][j]=='?') continue;
				if(!used[i][j]){
					//printf("i %d j %d\n",i,j);
					int u=i-1,d=i+1;
					used[i][j]=1;
					while(u>=0&&(g[u][j]=='?'||g[u][j]==g[i][j])){
						//printf("u %d\n",u);
						used[u][j]=1;
						g[u][j]=g[i][j];
						u--;
					}
					while(d<r&&(g[d][j]=='?'||g[d][j]==g[i][j])){
						//printf("d %d\n",d);
						used[d][j]=1;
						g[d][j]=g[i][j];
						d++;
					}
					u++;
					d--;
					//printf("%d %d\n",u,d);
					int t=j+1;
					while(t<c&&check(u,d,t,g[i][j])){
						for(int k=u;k<=d;k++){
							g[k][t]=g[i][j];
							used[k][t]=true;
						}
						t++;
					}
					t=j-1;
					while(t>=0&&check(u,d,t,g[i][j])){
						for(int k=u;k<=d;k++){
							g[k][t]=g[i][j];
							used[k][t]=true;
						}
						t--;
					}
				}
				//printf("#%d %d\n",r,c);
			}
		}
		printf("Case #%d:\n",cases);
		for(int i=0;i<r;i++){
			printf("%s\n",g[i]);
		}
	}
	return 0;
}
