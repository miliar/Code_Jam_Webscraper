#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<time.h>
#include<assert.h>
#include<iostream>
using namespace std;
typedef long long LL;
typedef pair<int,int>pi;
char s[2000];
int k;
int main(){
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	int _;scanf("%d",&_);
	int cas=1;
	while(_--){
		scanf("%s%d",s,&k);
		int n=strlen(s);
		int ans=0;
		for(int i=k-1;i<n;i++){
			if(s[i-k+1]=='-'){
				ans++;
				for(int j=i-k+1;j<=i;j++){
					if(s[j]=='-')s[j]='+';
					else s[j]='-';
				}
			}
		}
		for(int i=0;i<n;i++)if(s[i]=='-')ans=-1;
		printf("Case #%d: ",cas++);
		if(ans<0)puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
	return 0;
}
