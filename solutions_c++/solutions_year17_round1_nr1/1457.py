#include <bits/stdc++.h>
using namespace std;

int t,r,c;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		scanf("%d%d",&r,&c);
		char grid[30][30],cur;
		for(int i=0;i<r;i++) for(int j=0;j<c;j++) cin>>grid[i][j];
		for(int i=0;i<r;i++) {
			for(int j=0;j<c;j++){
				if(grid[i][j]!='?'){
					cur=grid[i][j];
					for(int a=j+1;a<c;a++){
						if(grid[i][a]=='?') grid[i][a]=cur;
						else break;
					}
					for(int a=j-1;a>=0;a--){
						if(grid[i][a]=='?') grid[i][a]=cur;
						else break;
					}
				}
			}
		}
		for(int i=0;i<r;i++) {
			for(int j=0;j<c;j++){
				if(grid[i][j]!='?'){
					cur=grid[i][j];
					for(int a=i+1;a<r;a++){
						if(grid[a][j]=='?') grid[a][j]=cur;
						else break;
					}
					for(int a=i-1;a>=0;a--){
						if(grid[a][j]=='?') grid[a][j]=cur;
						else break;
					}
				}
			}
		}
		printf("Case #%d:\n",tc);
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++) cout<<grid[i][j];
			printf("\n");
		}
	}
}
