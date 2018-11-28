#include<bits/stdc++.h>
using namespace std;

int T,R,C,dp[30][30];
char carr[30][30];

int getnum(int x1, int y1, int x2, int y2){
	int num=dp[x2][y2];
	if (x1>x2 || y1>y2) return 1;
	if (x1>0) num-=dp[x1-1][y2];
	if (y1>0) num-=dp[x2][y1-1];
	if (x1>0 && y1>0) num+= dp[x1-1][y1-1];
	//printf("%d %d %d %d   %d\n",x1,y1,x2,y2,num);
	return num;
}

void process (int x1, int y1, int x2, int y2){
int i,j;
	if(getnum(x1,y1,x2,y2)==1){
		if (x1<=x2 && y1<=y2){
			//printf("%d %d %d %d\n",x1,y1,x2,y2);
			char c;
			for (int i=x1;i<=x2;i++){
				for (int j=y1;j<=y2;j++){
					if (carr[i][j]!='?') c=carr[i][j];
				}
			}
			for (int i=x1;i<=x2;i++){
				for (int j=y1;j<=y2;j++) carr[i][j]=c;
			}			
		}
	} else {
		i=x1; j=y1;
		while (getnum(x1,y1,i,j)==0 || getnum(x1,j+1,i,y2)==0 || getnum(i+1,y1,x2,j)==0 || getnum(i+1,j+1,x2,y2)==0){
		//	printf("%d %d %d %d %d %d\n",x1,y1,i,j,x2,y2);
		//	printf("%d %d %d %d\n",getnum(x1,y1,i,j),getnum(x1,j+1,i,y2),getnum(i+1,y1,x2,j),getnum(i+1,j+1,x2,y2));
			j++;
			if (j==y2+1) {
				j=y1;
				i++;
			}
		}
		process(x1,y1,i,j);
		process(x1,j+1,i,y2);
		process(i+1,y1,x2,j);
		process(i+1,j+1,x2,y2);
	}
}

int main(){
	freopen("cake.in","r",stdin);
	freopen("cake.out","w",stdout);
	scanf("%d",&T);
	for (int i=1; i<=T; i++){
		scanf("%d%d",&R,&C);
		for (int j=0; j<R; j++){
			scanf(" %s",&carr[j]);
		}
		for (int j=0; j<R; j++){
			for (int k=0; k<C; k++) {
				if (j>0 && k>0)	dp[j][k]=dp[j-1][k-1];
				else dp[j][k]=0;
				for (int l=0;l<=j;l++){
					if (carr[l][k]!='?') dp[j][k]++;
				}
				for (int l=0;l<k;l++){
					if (carr[j][l]!='?') dp[j][k]++;
				}
			}
		}
		process(0,0,R-1,C-1);
		printf("Case #%d:\n",i);
		for (int j=0;j<R;j++){
			for (int k=0; k<C; k++) printf("%c", carr[j][k]); printf("\n");
		}
	}
	return 0;
}
