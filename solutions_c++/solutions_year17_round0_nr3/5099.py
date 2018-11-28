#include <bits/stdc++.h>
using namespace std;

void solve(int N, int K){
	priority_queue<int> Q;
	int L = 0, R = N-1;
	Q.push(N);
	int x;
	while(K--){
		x = Q.top();
		Q.pop();
		if(x%2==1)
			Q.push(x/2);
		else
			Q.push(x/2-1);
		Q.push(x/2);
	}
	printf("%d ", x/2);
	if(x%2==1)
		printf("%d\n", x/2);
	else
		printf("%d\n", x/2-1);
}

int main(){
	int T,K,N;
	scanf("%d",&T);
	for(int i = 1; i <= T; i++){
		scanf("%d%d",&N,&K);
		printf("Case #%d: ",i); solve(N,K);
	}
	return 0;
}