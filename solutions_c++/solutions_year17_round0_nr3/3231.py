#include <bits/stdc++.h>
#define lld long long

using namespace std;

lld N,K;
map<lld,lld> Map;

void process(){
	scanf("%lld %lld",&N,&K);
	priority_queue<lld> q; q.push(N);
	lld sum = 0;
	Map.clear(); Map[N] = 1;
	while(true){
        lld x = q.top();
		q.pop();
		sum += Map[x];
		lld t1,t2;
		t1 = (x-1)/2;
		t2 = x-t1-1;
		if(sum >= K){
			printf("%lld %lld\n",max(t1,t2),min(t1,t2));
			break;
		}
		if(Map[t1] == 0) q.push(t1);
		Map[t1] += Map[x];
		if(Map[t2] == 0) q.push(t2);
		Map[t2] += Map[x];
	}
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
