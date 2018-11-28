#include<stdio.h>
#include<string.h>

char str[22];

int main(){

	int t,count=1;
	int len,i,j;
	scanf("%d",&t);
	while(t--){
		scanf("%s",str);
		len=strlen(str);
		while(1){
			for(i=0;i<len-1;i++){
				if(str[i]>str[i+1]){
					str[i]--;
					for(j=i+1;j<len;j++) str[j]='9';
					break;
				}
			}
			if(i==len-1) break;
		}
		printf("Case #%d: ",count++);
		if(str[0]!='0') printf("%c",str[0]);
		for(i=1;i<len;i++) printf("%c",str[i]);
		printf("\n");
	}
	return 0;
}