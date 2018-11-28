/*
 * stalls.cc
 *
 *  Created on: Apr 8, 2017
 *      Author: maciek
 */
#include <queue>
#include <iostream>

using namespace std;




int main(){
	int T;
	cin >> T;

    long long N, K;
	for(int i = 0; i < T; i++){
		cin >> N >> K;
		priority_queue<long long> q;
		q.push(N);
		int x;
		for(long long j = 0; j < K-1; j++ ){
			x = q.top();
			q.pop();
			if(x % 2 == 1){
				q.push(x/2);
				q.push(x/2);
			}else{
				q.push(x/2 - 1);
				q.push(x/2);
			}
		}
		x = q.top();
		q.pop();
		cout << "Case #" << i+1 << ": ";
		if(x % 2 == 1)
			cout << x/2 << " " << x/2 << endl;
		else
			cout << x/2 << " " << x/2 - 1 << endl;
	}

}





