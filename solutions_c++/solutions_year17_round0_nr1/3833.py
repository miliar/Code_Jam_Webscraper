#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#define inputt int t;cin>>t;
#define pi acos(-1.0)
#define lson o*2,l,m
#define rson o*2+1,m+1,r
#define INF 0x7f7f7f7f
#define lowbit(X) ((X)&(-X))
#define clr(X,Y) memset(X,Y,sizeof(X))
typedef long long ll;
using namespace std;
char s[1005];
int main(){
	inputt
	for(int cas=1;cas<=t;cas++){
		int k;
		scanf("%s%d",s,&k);
		
		int len=strlen(s);
		int ans=0;
		for(int i=0;i<=len-k;i++){
			if(s[i]=='-'){
				for(int j=0;j<k;j++){
					if(s[i+j]=='-')s[i+j]='+';
					else s[i+j]='-'; 
				}
				ans++;
			}
		}
		int flag=0;
		for(int i=len-k+1;i<len;i++)if(s[i]=='-')flag=1;
		printf("Case #%d: ",cas);
		if(flag)printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
	return 0;
}

