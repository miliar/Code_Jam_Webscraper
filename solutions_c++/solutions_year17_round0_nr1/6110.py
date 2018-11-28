
#include <stdio.h>
#include <string.h>


int l;
char S[10000];
int T;
int C;
int k,j,i,ans,flag,m;
int main() {
	scanf("%d", &T);
	while (T--) {
		scanf("%s%d", S,&k);
		l = strlen(S);
		flag=0;
		printf("Case #%d: ", ++C);
		ans = 0;
		for (i = 0; i <= l-k; i++)
		
		{
			if(S[i]=='-'){
				for(j=0;j<k;j++){
				
						if(S[i+j]=='+')
						S[i+j]='-';
						else
						S[i+j]='+';
				}
			ans++;	
		}
		//printf("%s\n",S);
		
	}
		
		if(strchr(S,'-'))
		printf("IMPOSSIBLE\n");
		else
		printf("%d\n", ans);
		
	}
}
