#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,k,len,ans;
	char s[1001];
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		ans=0;
		scanf("%s %d",s,&k);
		len=strlen(s);
		for(int j=0;j<=len-k;j++){
			if(s[j]=='-'){
				ans++;
				for(int l=j;l<j+k;l++){
					if(s[l]=='-') s[l]='+';
					else s[l]='-';
				}
			}
		}
		bool p=true;
		for(int j=0;j<len;j++){
			if(s[j]=='-') p=false;
		}
		if(p) printf("Case #%d: %d\n",i,ans);
		else printf("Case #%d: IMPOSSIBLE\n",i);
	}
	return 0;
}
