#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
using namespace std;
int T,n,m;
char s[30][30];
void init(){
	scanf("%d%d",&n,&m);
	int i;
	for(i=1;i<=n;i++){
		scanf("%s",s[i]+1);
		}
	}
void doit(){
	int i,j,k;
	for(j=1;j<=m;j++){
		i=n;
		while(s[i][j]=='?'&&i>0) i--;
		if(i>0){
			for(k=i;k<=n;k++) s[k][j]=s[i][j];
			k=i;
			while(i>0){
				if(s[i][j]=='?') s[i][j]=s[k][j];
				else k=i;
				i--;
				}
			}
		}
	for(j=2;j<=m;j++){
		if(s[1][j]=='?'){
			for(i=1;i<=n;i++) s[i][j]=s[i][j-1];
			}
		}
	for(j=m-1;j>0;j--){
		if(s[1][j]=='?'){
			for(i=1;i<=n;i++) s[i][j]=s[i][j+1];
			}
		}
	for(i=1;i<=n;i++)
	    puts(s[i]+1);
	return;
	}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(int k=1;k<=T;k++){
		printf("Case #%d:\n", k);
		init();
		doit();
		}
	return 0;
	}
