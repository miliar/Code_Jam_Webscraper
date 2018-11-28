#include <iostream>
#include <queue> 
using namespace std;

int T;
priority_queue<int> q;

int main(){
	cin >> T;
	for (int t = 1; t<=T; t++){
		cout << "Case #" << t << ": ";
		int N, K;
		cin >> N >> K;
		q.push(N);
		for(int i=0; i<K-1; i++){
			
			int curr = q.top();
			//cout << "curr: " << curr << " i: " << i << endl;
			if (curr%2==1){
				//cout << (curr-1)/2 << " " << (curr-1)/2;
				q.push((curr-1)/2);
				q.push((curr-1)/2);
			} 
			else{
				//cout << curr/2 << " " << (curr-1)/2;
				q.push(curr/2);
				q.push((curr/2)-1);
			}
			q.pop();
		}
		int curr = q.top();
		if (curr%2==1){
			cout << (curr-1)/2 << " " << (curr-1)/2;
		} 
		else{
			cout << curr/2 << " " << (curr/2)-1;
		}
		cout << endl;
		while(!q.empty()) q.pop();
	}
	
}
