#include <bits/stdc++.h>
using namespace std;
char s[1010];
int k;

void fuck()
{
	int i,j,l,cnt=0;
	scanf("%s%d",s+1,&k);
	l=strlen(s+1);
	for(i=1;i<=l;i++){
		if(s[i]=='-'){
			++cnt;
			if(i+k-1>l) break;
			for(j=0;j<k;j++){
				if(s[i+j]=='-') s[i+j]='+';
				else s[i+j]='-';
			}
		}
	}
	if(i<=l) printf("IMPOSSIBLE\n");
	else printf("%d\n",cnt);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		fuck();
	}
 return 0;
}

