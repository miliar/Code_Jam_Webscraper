#include<iostream>
#include<cstdio>
using namespace std;

int vis[210], match[210], adj[210][210];
int n; 

int aug(int l){
	if(vis[l]==1){
		return 0;
	}
	vis[l]=1;
	for(int j=0;j<=2*n-2;j++){
		if(adj[l][j]==1&&(match[j]==-1||aug(match[j]))){
			match[j]=l;
			//printf("match %d with %d\n", l, j);
			return 1;
		}
	}
	return 0;
}
	

int main(){
	int t, m;	
	char c;
	int a, b, score, cnt;
	int plus[105][105], times[105][105];//0:unknown, 1:given, 2:added, -1:not
	scanf(" %d", &t);
	for(int tcase=1;tcase<=t;tcase++){
		score=0;
		cnt=0;
		printf("Case #%d: ", tcase);
		scanf(" %d %d", &n, &m);
		//printf("input n=%d, m=%d OK\n", n, m);
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				plus[i][j]=0;
				times[i][j]=0;
			}
		}
		//printf("init plus times OK\n");
		for(int i=1;i<=m;i++){
			//printf("going to input\n");
			scanf(" %c %d %d", &c, &a, &b);
			//printf("input one line\n");
			if(c=='+'||c=='o'){
				plus[a][b]=1;
				score++;
			}
			if(c=='x'||c=='o'){
				times[a][b]=1;
				score++;
				for(int j=1;j<=n;j++){
					if(j!=b){
						times[a][j]=-1;
					}
					if(j!=a){
						times[j][b]=-1;
					}
				}
			}
		}
		//printf("input OK\n");
		//x
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				if(times[i][j]==0){
					times[i][j]=2;
					cnt++;
					score++;
					for(int temp=1;temp<=n;temp++){
						if(temp!=i){
							times[temp][j]=-1;
						}
						if(temp!=j){
							times[i][temp]=-1;
						}
					}
				}
			}
		}
		
		/*printf("times table\n");
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				printf("%d ", times[i][j]);
			}
			printf("\n");
		}
		*/
		
		//+, adj[i-j+n-1][i+j-2]
		for(int x=0;x<=2*n-2;x++){
			for(int y=0;y<=2*n-2;y++){
				if((x+y-n+3)%2==0&&(x+y-n+3)/2<=n&&(x+y-n+3)/2>=1&&(y-x+n+1)/2>=1&&(y-x+n+1)/2<=n){
					adj[x][y]=1;
				}
				else{
					adj[x][y]=0;
				}
			}
		}
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				if(plus[i][j]==1){
					for(int temp=0;temp<=2*n-2;temp++){
						adj[i-j+n-1][temp]=0;
						adj[temp][i+j-2]=0;
					}
				}
			}
		}
		for(int y=0;y<=2*n-2;y++){
			match[y]=-1;
		}
		for(int x=0;x<=2*n-2;x++){
			for(int temp=0;temp<=2*n-2;temp++){
				vis[temp]=0;
			}
			aug(x);
		}
		for(int y=0;y<=2*n-2;y++){
			if(match[y]!=-1){
				plus[(match[y]+y-n+3)/2][(y-match[y]+n+1)/2]=2;
				score++;
				if(times[(match[y]+y-n+3)/2][(y-match[y]+n+1)/2]!=2){
					cnt++;
				}
			}
		}
		
		//output
		printf("%d %d\n", score, cnt);
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				if((plus[i][j]==2||times[i][j]==2)&&times[i][j]!=-1&&plus[i][j]!=0){
					printf("o %d %d\n", i, j);
				}
				else if(plus[i][j]==2){
					printf("+ %d %d\n", i, j);
				}
				else if(times[i][j]==2){
					printf("x %d %d\n", i, j);
				}
			}
		}
	}
	return 0;
}

