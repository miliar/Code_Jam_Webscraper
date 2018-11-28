#include<bits/stdc++.h>
using namespace std;
int T,i,j,n,m;
char s[100][100];
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++){ 
			scanf("%s",s[i]+1);
			for(j=1;j<=m;j++)if(s[i][j]!='?')break;
			if(j<=m)s[i][1]=s[i][j];
		}
		for(i=1;i<=n;i++)if(s[i][1]!='?')break;
		for(j=1;j<=m;j++)s[1][j]=s[i][j];
		for(i=1;i<=n;i++){
			if(s[i][1]=='?')
				for(j=1;j<=m;j++)s[i][j]=s[i-1][j];
			for(j=1;j<=m;j++)
				if(s[i][j]=='?')s[i][j]=s[i][j-1];
		}
		printf("Case #%d: \n",_);
		for(i=1;i<=n;i++)puts(s[i]+1);
	}
}
