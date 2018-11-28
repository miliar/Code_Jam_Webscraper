#include<bits/stdc++.h>
using namespace std;
char s[3000];
int main(){
	int T;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		int k,ans=0,n;
		scanf("%s %d",s,&k);
		n=strlen(s);
		for(int i=0;s[i];i++){
			if(s[i]=='-'){
				if(i+k<=n){
					ans++;
					for(int j=i;j<i+k;j++){
						if(s[j]=='-') s[j]='+';
						else s[j]='-';
					}
				}
				else{
					ans=-1;
					break;
				}
			}
		}
		if(ans>=0)
			printf("Case #%d: %d\n",cs,ans);
		else 
			printf("Case #%d: IMPOSSIBLE\n",cs);
	}
	return 0;
}
