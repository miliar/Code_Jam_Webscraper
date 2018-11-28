#include<bits\stdc++.h>
using namespace std;
main(){
	int i,T,k;
	char s[1100];
	freopen("A-large.in","r",stdin);
	freopen("outputA2.out","w",stdout);
	scanf("%d",&T);
	for(int m=1;m<=T;m++){
		scanf("%s %d",&s,&k);
		int l=strlen(s);
		int ans=0;
		for(i=0;i<=l-k;i++){
			if(s[i]=='-'){
				ans++;
				for(int j=0;j<k;j++){
					if(s[j+i]=='+') s[j+i]='-';
					else s[j+i]='+';
				}
			}
		}
		for(i=0;i<l;i++){
			if(s[i]=='-') break;
		}
		if(i==l){
			printf("Case #%d: %d\n",m,ans);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n",m,ans);
		}
	}
}
