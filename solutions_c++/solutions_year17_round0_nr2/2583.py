#include<bits/stdc++.h> 
using namespace std;
int T,n,i,l,j;
char s[100];
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		scanf("%s",s+1);
		n=strlen(s+1);
		s[n+1]='9'+1;
		for(i=1;i<=n;i++)if(s[i+1]<s[i])break;
		for(s[i]--;s[i]<s[i-1]&&i;s[--i]--);
		for(j=i+1;j<=n;j++)s[j]='9';
		printf("Case #%d: ",_);
		for(i=1+(s[1]=='0');i<=n;i++)printf("%c",s[i]);
		puts("");
	}
}
