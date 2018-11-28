#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

void solve(){
	int K;
	char lho[1101];
	scanf("%s", lho);
	scanf("%d",&K);
	int N = strlen(lho);
	int flip = 0;
	for (int i=0;i<N;i++){
		if (lho[i] == '-'){
			if (i + K - 1>= N){
				printf("IMPOSSIBLE\n");
				return;
			}
			for (int j=i;j<i+K;j++){
				if (lho[j]=='-')
					lho[j]= '+';
				else 
					lho[j]= '-';
			}
			flip++;
		}
	}
	printf("%d\n", flip);
}

int main(){
	int T;
	scanf("%d",&T);
	for (int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		solve();
	}
}