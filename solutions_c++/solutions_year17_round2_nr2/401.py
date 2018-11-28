#include<stdio.h>
#include<string.h>
char ans[10000],s[]="ROYGBV";
int len,n,a[6];
void DO(){
	int i,j,k;
	for(i=0;i<6;i+=2){
		if(a[i])
			break;
	}
	a[i]--;
	ans[len++]=s[i];
	while(len!=n){
		//printf("%c\n",s[i]);
		if(i%2==0){
			if(a[(i+3)%6])
				i = (i+3)%6;
			else{
				j = (i+2)%6;
				k = (i+4)%6;
				if(a[j]>a[k])
					i = j;
				else if(a[j]<a[k])
					i = k;
				else if(j<k)
					i = j;
				else
					i = k;
			}
		}
		else{
			i = (i+3)%6;
		}
		if(a[i]==0){
			strcpy(ans,"IMPOSSIBLE");
			return;
		}	
		a[i]--;
		ans[len++]=s[i];
	}
	ans[len] = 0;
	if(ans[len-1]==ans[0])
		strcpy(ans,"IMPOSSIBLE");
}
int main(){
	int T,t,i;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d",&n);
		len = 0;
		for(i=0;i<6;i++)
			scanf("%d",&a[i]);
		DO();	
		printf("Case #%d: %s\n",t,ans);
		
	}
}
