#include<bits/stdc++.h>
#define N 1010
using namespace std;
char s[N];
int n,k;
int main(){int cnt=0;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;scanf("%d",&T);
	while(T--){
		printf("Case #%d: ",++cnt);
		scanf("%s%d",s,&k);
		int len=strlen(s);int ans=0,rev=0;
		for(int i=0;i<len;i++){
			if(rev==-1)break;
			if(s[i]=='-'){
				if(i+k>len){puts("IMPOSSIBLE");rev=-1;break;}
				ans++;rev++;
				for(int j=i;j<=i+k-1;j++)if(s[j]=='+')s[j]='-';else s[j]='+';
			}
		}
		if(rev!=-1)printf("%d\n",ans);
	}
	return 0;
}
