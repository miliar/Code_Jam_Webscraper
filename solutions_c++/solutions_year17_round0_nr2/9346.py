#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
typedef long long ll;

char s[20];
char ans[20];


int main() {
	
//	freopen("ansbig.out","w",stdout);
	int t;
	ll n;

	int cas=1;
	scanf("%d",&t);
	while(t--) {
		memset(ans,0,sizeof(ans));
		scanf("%s",s);
		int l=strlen(s);
		int flag=0;
		for(int i=l-1;i>=0;i--){
			if(i==0&&flag) ans[i]=s[i]-1;
			
			
			if(s[i-1]>=s[i]&&flag){
				ans[i]='9';
				ans[i-1]=s[i-1]-1;
			
			
			}
			else if(s[i-1]>s[i]){
				ans[i]='9';
				flag=1;
			}
			
			else {
				if(flag)
					ans[i]=s[i]-1;
				else
					ans[i]=s[i];
				flag=0;	
			}
		}
		
	
		for(int i=1;i<l-1;i++){
			if(ans[i]>ans[i+1]) ans[i+1]=ans[i];
		}
		
		if(ans[0]=='0'){
			printf("Case #%d: ",cas++);
			for(int i=1;ans[i];i++) printf("%c",ans[i]);
			puts("");
		}
	
		else	
			printf("Case #%d: %s\n",cas++,ans);
	}
}
