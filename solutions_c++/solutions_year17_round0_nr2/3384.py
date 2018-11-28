#include <stdio.h>
#include <string.h>

int main(){
	int T;
	scanf("%d",&T);
	for(int t=0; t<T; t++){
		char S[20];
        int s[20];
		scanf(" %s",S);
		for(int i=0; i<strlen(S); i++)
			s[i] = S[i]-'0';
		for(int i=0; i<strlen(S)-1; i++)
			if(s[i]>s[i+1]){
				s[i]--;
				for(int j=i+1; j<strlen(S); j++)
					s[j] = 9;
                int k=i-1;
                while(k>=0 && s[k]>s[k+1]){
                    s[k]--;
                    s[k+1] = 9;
                    k--;
                }
				break;
			}
		long long ans = 0;
		for(int i=0; i<strlen(S); i++){
			ans *= 10;
			ans += s[i];
		}
		printf("Case #%d: %lld\n",t+1,ans);
	}
	return 0;
}
