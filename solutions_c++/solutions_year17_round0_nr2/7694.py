#include <stdio.h>
#include <string.h>

int main(){
	
	freopen("B-large.in", "r", stdin);
	freopen("file.out", "w", stdout);
	
	int T; scanf("%d", &T);
	
	char S[55];
	
	for(int ct = 1; ct <= T; ++ct){
		
		scanf("%s", S);
		
		int len = strlen(S);
		
		int p = -1;
		
		for(int i = 0; i < len - 1; ++i){
			if(S[i] > S[i + 1]){
				p = i;
				break;
			}
		}
		
		if(p >= 0){
			while(p > 0 && (S[p] - 1) < S[p - 1]){
				p--;
			}
			
			if(p == 0 && S[p] == '1'){
				len--;
				S[len] = '\0';
				for(int i = 0; i < len; ++i)
					S[i] = '9';
			}else{
				S[p]--;
				for(int i = p + 1; i < len; ++i)
					S[i] = '9';
			}
		}
		
		printf("Case #%d: %s\n", ct, S);
	}
	
	
return 0;	
}
