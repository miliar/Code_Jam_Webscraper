#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstring>
#include <set>
#include <queue>
#include <sstream>
#include <stack>

using namespace std;

int main(){
	int T;
	cin>>T;
	for(int casenum=1; casenum<=T; casenum++){
		int N,K;
		cin>>N>>K;
	
		priority_queue<int> pq;
		int mid = (1+N+2)/2;
		int minl = min(mid-1, N+2-mid);
		int maxl = N+1-minl;
	//	cout<<"mid = "<<mid<<endl;
		if(minl > 1)
			pq.push(minl);
		if(maxl >1)
			pq.push(maxl);
		K--;
		if(K==0){
			printf("Case #%d: %d %d\n", casenum, maxl-1, minl-1);
			continue;
		}
		
		while(K){
			int cur = pq.top(); pq.pop();
			K--;
			mid = cur/2;
			minl = min(cur-mid, mid);
			maxl = cur-minl;
			if(K==0){
				printf("Case #%d: %d %d\n", casenum, maxl-1, minl-1);
				break;
			}
			if(minl>1) pq.push(minl);
			if(maxl>1) pq.push(maxl);
		}
	}
	return 0;
}