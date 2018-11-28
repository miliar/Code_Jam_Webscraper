#include<bits/stdc++.h>
using namespace std;

int T,N,K;
priority_queue<int> pq;

int main(){
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>N>>K;
		while(!pq.empty())
			pq.pop();
		pq.push(N);
		for(int i=0;i<K-1;i++){
			int x = pq.top();
			pq.pop();
			int y= x/2;
			int z = x - y - 1;
			if(y!=0)
				pq.push(y);
			if(z!=0)
				pq.push(z);
		}
		int x = pq.top();
		pq.pop();
		int y= x/2;
		int z = x - y - 1;
		printf("Case #%d: %d %d\n",t,max(y,z),min(y,z));
	}
}