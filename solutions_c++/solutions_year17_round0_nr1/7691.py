#include <stdio.h>
#include <string.h>

int main(){
	
	freopen("A-large.in", "r", stdin);
	freopen("file.out", "w", stdout);
	
	int T; scanf("%d", &T);
	
	char S[1111];
	int K;
	
	for(int ctor = 1; ctor <= T; ++ctor){
		
		scanf("%s %d", S, &K);
		
		int len = strlen(S);
		
		int ans = 0;
		
		for(int i = 0; i <= len - K; ++i){
			if(S[i] == '-'){
				ans++;
				
				for(int j = i; j < i + K; ++j)
					if(S[j] == '-')
						S[j] = '+';
					else
						S[j] = '-';
			}
		}
		
		int ok = 1;
		for(int i = len - K + 1; i < len; ++i)
			if(S[i] == '-')
				ok = 0;
					
		printf("Case #%d: ", ctor);
		
		if(ok)
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	
	}
	
return 0;	
}
