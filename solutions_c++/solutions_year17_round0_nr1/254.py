#include <stdio.h>

int t,s[1024];
char c;
int resp,n;

int main(){
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		resp=n=0;
		scanf(" %c",&c);
		while(c=='+' || c=='-'){
			s[n]=(c=='-');
			n++;
			scanf("%c",&c);
		}
		int k;
		scanf("%d",&k);
		
		for(int i=0;i<=n-k;i++){
			if(s[i]){
				resp++;
				for(int j=0;j<k;j++){
					s[i+j]^=1;
				}
			}
		}
		bool foi=true;
		for(int i=0;i<n && foi;i++){
			if(s[i]) foi=false;
		}
		if(foi) printf("Case #%d: %d\n",tt,resp);
		else printf("Case #%d: IMPOSSIBLE\n",tt);
	}
	return 0;
}
		
