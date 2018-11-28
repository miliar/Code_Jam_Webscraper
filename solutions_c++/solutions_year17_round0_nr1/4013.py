#include <bits/stdc++.h>
using namespace std;

int main(){

	freopen("input.txt","r",stdin);
	// freopen("p1B_17_output.txt","w",stdout);
	freopen("p1B_17_outputLarge.txt","w",stdout);

	int t,n,count,flag;

	scanf("%d",&t);

	for(int i=1;i<=t;i++){

		char s[1025]="";
		// printf("%s ",s);
		scanf("%s",s);
		scanf("%d",&n);
		flag=count=0;
		for(int j=0;j<strlen(s);j++){
			if(s[j]=='-'){
				// printf("%d ",j);
				if(j+n-1<strlen(s)){
					// printf("%d ",j+n-1);
					for(int k=j;k<j+n;k++)
						s[k] = (s[k]=='-')?'+':'-';
					count++;
				}else{
					flag=1;
					break;
				}
			}
		}
		if(flag)
			printf("Case #%d: IMPOSSIBLE\n",i);
		else
			printf("Case #%d: %d\n",i,count);
	}
	return 0;
}