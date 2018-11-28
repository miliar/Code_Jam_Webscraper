#include <bits/stdc++.h>

void process(){
	int N,K,ans = 0;
	char s[10000];
    scanf("%s",s);
    scanf("%d",&K);
    N = strlen(s);
    for(int i=0; i+K-1<=N-1; i++){
        if(s[i] == '-'){
            for(int j=i; j<i+K; j++){
				if(s[j] == '+') s[j] = '-';
				else s[j] = '+';
            }
            ans++;
        }
    }
    for(int i=0; i<N; i++){
		if(s[i] == '-'){
			printf("IMPOSSIBLE\n");
			return;
		}
    }
    printf("%d\n",ans);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int i=1; i<=T; i++){
		printf("Case #%d: ",i);
		process();
	}

	return 0;
}
