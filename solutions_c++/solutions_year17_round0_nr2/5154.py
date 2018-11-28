#include <bits/stdc++.h>
using namespace std;

int main(){
	int T = 0;
	scanf("%d", &T);
	
	for(int i = 1; i <= T; i++){
		long long N = 0;
		scanf("%llu", &N);
		
		char S[20];
		sprintf(S, "%llu", N);
		
		while(1){
			bool TIDY = true;
			for(int j = 0; j < strlen(S)-1; j++){
				if(S[j] <= S[j+1]) continue;
				
				TIDY = false;
				S[j]--;
				for(int k = j+1; k < strlen(S); k++) S[k] = '9';
				break;
			}
			
			if(TIDY) break;
		}
		
		printf("Case #%d: ", i);
		if(S[0] != '0') printf("%c", S[0]);
		for(int j = 1; j < strlen(S); j++)
			printf("%c", S[j]);
		
		puts("");
	}
	return 0;
}