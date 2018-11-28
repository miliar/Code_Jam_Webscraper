#include <bits/stdc++.h>
using namespace std;
char s[20];

void fuck()
{
	int i,j,l;
	scanf("%s",s+1);
	l=strlen(s+1);
	for(i=1;i<l;i++){
		if(s[i]>s[i+1]) break;
	}
	if(i==l){
		printf("%s\n",s+1);
		return;
	}
	for(j=i;j>=1;j--){
		if(s[j]!=s[j-1]) break;
	}
	s[j]--;
	for(i=j+1;i<=l;i++) s[i]='9';
	if(s[j]=='0'){
		printf("%s\n",s+2);
		return;
	}
	printf("%s\n",s+1);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		fuck();
	}
 return 0;
}

