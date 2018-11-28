#include<stdio.h>
#include<string.h>
#define N 1002

char str[N];

int main(){

	int t,n,len;
	int i,j,count=1,ans;
	scanf("%d",&t);
	while(t--){
		scanf("%s %d",str,&n);
		len=strlen(str);
		ans=0;
		for(i=0;i<=len-n;i++){
			if(str[i]=='-'){
				for(j=i;j<i+n;j++)
					str[j]=str[j]=='+'?'-':'+';
				ans++;
			}
		}
		for(;i<len;i++){
			if(str[i]=='-') break;
		}
		if(i==len) printf("Case #%d: %d\n",count++,ans);
		else printf("Case #%d: IMPOSSIBLE\n",count++);
	}
	return 0;
}



