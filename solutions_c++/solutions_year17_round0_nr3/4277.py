#include <bits/stdc++.h>
using namespace std;
int n,k;
priority_queue<int> Q;

void input(void){
	scanf("%d %d",&n,&k);
}

void process(void){
	int i,x,y;
	while(!Q.empty()) Q.pop();
	Q.push(n);
	for(i=1;i<=k;i++){
		int t=Q.top(); Q.pop();
		x=(t-1)/2;
		y=t/2;
		Q.push(x); Q.push(y);
	}
	printf("%d %d\n",y,x);
}

int main(){
	freopen("input.txt","r",stdin);

	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		printf("Case #%d: ",i);
		input();
		process();
	}

	return 0;
}
