#include<bits/stdc++.h>
using namespace std;
char s[30][30];
int main(){
	int T,r,c;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		scanf("%d%d",&r,&c);
		for(int i=0;i<r;i++){
			scanf("%s",s[i]);
			for(int j=1;j<c;j++){
				if(s[i][j]=='?') s[i][j]=s[i][j-1];
			}
			for(int j=c-2;j>=0;j--){
				if(s[i][j]=='?') s[i][j]=s[i][j+1];
			}
		}
		for(int j=0;j<c;j++){
			for(int i=1;i<r;i++){
				if(s[i][j]=='?') s[i][j]=s[i-1][j];
			}
			for(int i=r-2;i>=0;i--){
				if(s[i][j]=='?') s[i][j]=s[i+1][j];
			}
		}
		printf("Case #%d:\n",cs);
		for(int i=0;i<r;i++){
			puts(s[i]);
		}
	}
	return 0;
}