#include <bits/stdc++.h>
using namespace std;
int n,m;
char s[30][30];

void fuck()
{
	int i,j,k;
	scanf("%d%d",&n,&m);
	for(i=1;i<=n;i++){
		scanf("%s",s[i]+1);
	}
	for(i=1;i<=n;i++){
		for(j=1;j<=m;j++){
			if(s[i][j]!='?'){
				for(k=j-1;k>0&&s[i][k]=='?';k--) s[i][k]=s[i][j];
				for(k=j+1;k<=m&&s[i][k]=='?';k++) s[i][k]=s[i][j];
			}
		}
	}
	for(i=2;i<=n;i++){
		for(j=1;j<=m;j++){
			if(s[i][j]=='?') memcpy(s[i],s[i-1],sizeof(s[i]));
		}
	}
	for(i=n-1;i>=1;i--){
		for(j=1;j<=m;j++){
			if(s[i][j]=='?') memcpy(s[i],s[i+1],sizeof(s[i]));
		}
	}
	for(i=1;i<=n;i++)
		printf("%s\n",s[i]+1);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		printf("Case #%d:\n",i);
		fuck();
	}
 return 0;
}

