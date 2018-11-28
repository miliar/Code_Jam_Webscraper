#include <stdio.h>
#include <string.h>
int main(){
	int i,tc;
    scanf("%d",&tc);
	char s[1001];
	for(i=0;i<tc;i++){
		int j,k,l,m;
		int cont=0;
		scanf("%s %d",s,&k);
		l=strlen(s);
        for(j=0;j<=l-k;j++){
			if(s[j]=='-'){
				for(m=j;m<j+k;m++){
					if(s[m]=='-')s[m]='+';
					else s[m]='-';
				}
				cont++;
			}
		}
		bool ok=1;
		for(j=0;j<l;j++){
			if(s[j]=='-'){
				ok=0;
				break;
			}
		}
		if(ok){
			printf("Case #%d: %d\n",i+1,cont);
		}else{
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		}
		
	}
	return 0;
}
