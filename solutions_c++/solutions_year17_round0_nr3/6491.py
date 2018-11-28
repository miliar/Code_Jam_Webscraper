#include <queue>
#include <iostream>
#include <cstdio>

using namespace std;


int main(){
	int i = 0;
	int T;
	scanf("%d",&T);
	for(i=1;i<=T;i++){
		int n;
		int k;
		scanf("%d%d",&n,&k);
		priority_queue <int> pq;
		pq.push(n);
		if(k==n){
			printf("Case #%d: 0 0\n",i);
			continue;
		}
		int lo,hi;
		for(int j = 0;j<k;j++){
			int lar = pq.top();
			pq.pop();
			if(lar%2 ==0){
				lo = lar/2;
				hi = lo-1;
			}
			else{
				lo = lar/2;
				hi = lar/2;
			}
			if(lo > 0)
				pq.push(lo);
			if(hi > 0)
				pq.push(hi);
		}
		
		printf("Case #%d: %d %d\n",i, lo, hi);
	}
	return 0;
}
