#include <bits/stdc++.h>
#define N 1005
using namespace std;
int n,k;
char s[N];
int main(){
	freopen("A-large.in","r",stdin); freopen("A.out","w",stdout);
	int t; scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		scanf("%s %d",s,&k); n=strlen(s);
		int ans=0;
		for(int i=0;i<n;i++){
			if (s[i]=='+') continue;
			if (i+k>n){
				ans=-1; break;
			}
			for(int j=i;j<i+k;j++) s[j]=(s[j]=='+'?'-':'+');
			ans++;
		}
		printf("Case #%d: ",tc);
		if (ans==-1) puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
}
