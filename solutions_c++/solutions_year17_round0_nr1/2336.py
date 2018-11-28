#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<cmath>
#define LL long long
using namespace std;
int T,k,ans,l;
char s[2100];
int main(){
	scanf("%d",&T);
	for (int I=1;I<=T;I++){
		scanf("%s%d",s,&k);
		ans=0;
		l=strlen(s);
		for (int i=0;i<=l-k;i++)
			if (s[i]=='-'){
				ans++;
				for (int j=0;j<k;j++) s[i+j]='+'+'-'-s[i+j];
			}
		for (int i=l-k+1;i<l;i++)
			if (s[i]=='-') ans=-1;
		if (ans==-1) printf("Case #%d: IMPOSSIBLE\n",I);
		else printf("Case #%d: %d\n",I,ans);
	}
    return 0;
}

