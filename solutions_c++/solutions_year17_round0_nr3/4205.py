#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;

void oneRun(){
	long long N, K;
	cin >> N >> K;
	priority_queue<pair<long, long> > Q;
	
	Q.push(make_pair(N,1));
	long long i = 0;
	while(i < K) {
		long k = Q.top().first; long u = Q.top().second;
		i += u;
		
		if(i >= K) {
			break;
		}
		
		Q.pop();
		
		if(k==1) {
			continue;
		} 
		if(k==2) {
			Q.push(make_pair(1,u));
			continue;
		}
		if(k % 2 == 0) {
			Q.push(make_pair(k/2,u));
			Q.push(make_pair(k/2-1,u));
		} else {
			Q.push(make_pair(k/2, 2*u));
		}
	}
	long k = Q.top().first;
	if(k % 2 == 0) {
		cout << k/2 << " " << k/2-1;
	} else {
		cout << k/2 << " " << k/2;
 	}
}

int main(){
	int nums;
	cin >> nums;
	for(int i=1; i <= nums; i++) {
		cout << "Case #" << i << ": ";
		oneRun();
		cout << endl;
	}
	return 0;
}