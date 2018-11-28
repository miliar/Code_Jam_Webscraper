/*
TASK: Tidy Number
*/
#include <bits/stdc++.h>
using namespace std;

int main(){
	int t,len,i,k,ch,j;
	char a[2000];
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		scanf(" %s",a);
		len = strlen(a);
		while(1){
			for(j=0;j<len-1;j++){
				if(a[j]>a[j+1]){
					a[j]--;
					for(k=j+1;k<len;k++)
						a[k]='9';
				}
			}
			ch=1;
			for(j=0;j<len-1;j++){
				//printf("%c",a[j]);
				if(a[j]>a[j+1]){
					ch=0;
					break;
				}
			}
		//	printf("\n");
			if(ch)	break;	
		}
		for(j=0;j<len&&a[j]=='0';j++);
		for(;j<len;j++)
			printf("%c",a[j]);
		printf("\n");
	}
	return 0;
}
