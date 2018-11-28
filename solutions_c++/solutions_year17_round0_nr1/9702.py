#include <stdio.h>
#include <string.h>

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;scanf("%d\n",&T);for(int Test=1;Test<=T;Test++){
		char a[1003];
		int K;
		scanf("%s%d\n",a, &K);
		int answer = 0;
		int N = strlen(a);
		int i;
		for(i=0;i<=N-K;i++){
			if(a[i] == '-'){
				for(int j=i;j<i+K;j++) a[j] = a[j]=='-'?'+':'-';
				answer++;
			}
		}
		for(;i<N;i++) if(a[i] == '-') break;
		if(i==N){
			printf("Case #%d: %d\n",Test, answer);
		}
		else {
			printf("Case #%d: IMPOSSIBLE\n", Test);
		}
	}
}