/*
TASK: Oversized Pancake Flipper
*/
#include <bits/stdc++.h>
using namespace std;

int main(){
	int t,len,i,k,ans,ch,j,l;
	char a[2000];
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		scanf(" %s %d",a,&k);
		len = strlen(a);
		ans=0;
		for(j=0;j<=len-k;j++){
			if(a[j]=='-'){
				ans++;
				for(l=0;l<k;l++){
					if(a[j+l]=='+')	a[j+l]='-';
					else			a[j+l]='+';
				}
			}
		}
		for(ch=0;j<len;j++)
			if(a[j]=='-')
				ch=1;
		if(ch)	printf("IMPOSSIBLE\n");
		else	printf("%d\n",ans);
	}
	return 0;
}
