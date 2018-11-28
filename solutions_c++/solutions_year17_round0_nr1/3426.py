#include <stdio.h>
#include <string.h>

int main(){
	int T;
	scanf("%d",&T);
	for(int t=0; t<T; t++){
		char s[1005];
        int S[1005];
		scanf(" %s",s);
		for(int i=0; i<strlen(s); i++){
			if(s[i] == '-')
				S[i] = 0;
			else
				S[i] = 1;
		}
		int K;
		scanf("%d",&K);
		int ans = 0;
		for(int i=0; i<=strlen(s)-K; i++)
			if(!S[i]){
				ans++;
				for(int j=i; j<i+K; j++)
					S[j] = !S[j];
			}
		int flg = 0;
		for(int i=strlen(s)-K; i<strlen(s); i++)
			if(!S[i])
				flg = 1;
		if(flg)
			printf("Case #%d: IMPOSSIBLE\n",t+1);
		else
			printf("Case #%d: %d\n",t+1,ans);
	}
	return 0;
}
