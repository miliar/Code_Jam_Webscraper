#include<stdio.h>
#include<string.h>
char a[19];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		scanf("%s",a);
		int siz=strlen(a);
		int j;
		for(j=siz-1;j;){
			int chk=-1,k;
			for(k=0;k<siz;k++){
				if(chk>a[k]-'0')break;
				chk=a[k]-'0';
			}
			if(k==siz)break;
			a[j]='9';
			while(--j&&a[j]=='0')a[j]='9';
			a[j]--;
		}
		printf("Case #%d: ",i+1);
		if(a[0]!='0')printf("%s\n",a);
		else printf("%s\n",a+1);
	}
	return 0;
}
