#include<stdio.h>
#include<stdlib.h>
int DO(char* s,int n){
	int c=0,i,j;
	for(i=0;s[i]!=0;i++){
		if(s[i]=='+')continue;
		for(j=0;j<n;j++){
			if(s[i+j]==0)
				return -1;
			if(s[i+j]=='+')
				s[i+j]='-';
			else
				s[i+j]='+';
		}
		c++;
	}
	return c;
}

int main(){
	int T,t;
	int n,ans;
	char s[10000];
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%s%d",s,&n);
		ans = DO(s,n);
		if(ans==-1)
			printf("Case #%d: IMPOSSIBLE\n",t);
		else
			printf("Case #%d: %d\n",t,ans);
	}
}
