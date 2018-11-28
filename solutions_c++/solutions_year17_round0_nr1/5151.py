#include <bits/stdc++.h>
using namespace std;

int main(){
	int T = 0;
	
	scanf("%d", &T);
	
	for(int i = 1; i <= T; i++){
	    char S[1001];
	    int K = 0;
	    int X = 0;
	    
		scanf("%s %d", S, &K);
		
		for(int j = 0; j <= strlen(S)-K; j++){
			if(S[j] == '+') continue;
			
			X++;
			
			for(int f = j; f < j+K; f++){
				if(S[f] == '-') S[f] = '+';
				else S[f] = '-';
			}
		}
		
		bool P =  true;
		
		for(int j = strlen(S)-K+1; j < strlen(S); j++){
			if(S[j] == '+') continue;
			
			P = false;
		}
		
		if(P) printf("Case #%d: %d\n", i, X);
		else printf("Case #%d: IMPOSSIBLE\n", i);
	}
	return 0;
}