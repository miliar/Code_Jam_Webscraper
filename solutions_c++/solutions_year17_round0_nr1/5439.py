#include<stdio.h>
#include<string.h>
char s[1001];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		int d;
		scanf("%s%d",s,&d);
		int cnt=0,siz=strlen(s);
		for(int j=0;j<=siz-d;j++){
			if(s[j]=='-'){
				cnt++;
				for(int k=j;k<j+d;k++)s[k]=(s[k]=='+'?'-':'+');
			}
		}
		int chk;
		for(chk=0;chk<siz;chk++)if(s[chk]=='-')break;
		printf("Case #%d: ",i+1);
		if(chk==siz)printf("%d\n",cnt);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
