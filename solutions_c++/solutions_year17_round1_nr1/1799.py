#include <bits/stdc++.h>

using namespace std;
int t,r,c,tc=0;
char M[30][30];
int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%d%d",&r,&c);
		for (int i=0;i<r;i++)
			scanf("%s",M[i]);
		bool flag=1,dir=0;
		while(1){
			flag=1;
			for (int i=0;i<r;i++)
				for (int j=0;j<c;j++)
					if (M[i][j]=='?')
						flag=0;
			if (flag) break;
			if (dir){
				for (int i=0;i<r;i++)
					for (int j=0;j<c;j++){
						int k=j+1;
						while(1){
							if (k>c) break;
							if (M[i][k]!='?') break;
							M[i][k]=M[i][j];
						    k++;
						}
						k=j-1;
						while(1){
							if (k<0) break;
							if (M[i][k]!='?') break;
							M[i][k]=M[i][j];
						    k--;
						}
					}
			}
			else{
				for (int i=0;i<r;i++)
					for (int j=0;j<c;j++){
						int k=i+1;
						while(1){
							if (k>r) break;
							if (M[k][j]!='?') break;
							M[k][j]=M[i][j];
						    k++;
						}
						k=i-1;
						while(1){
							if (k<0) break;
							if (M[k][j]!='?') break;
							M[k][j]=M[i][j];
						    k--;
						}
					}
			}
			dir=!dir;
		}
		printf("Case #%d:\n",++tc);
		for (int i=0;i<r;i++)
			printf("%s\n",M[i]);
	}
	return 0;
}
