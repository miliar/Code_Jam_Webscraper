#include <iostream>
#include <string>
#include <functional>
#include <vector>
#include <queue>

using namespace std;

int main(){
	int T;
	unsigned long long N, K;

	cin>>T;
	for(int i=0; i<T; i++){
		priority_queue<int> q;
		cin>>N>>K;
		q.push(N);
		cout<<"Case #"<<(i+1)<<": ";
		for(int j=0; j<K; j++){
			unsigned long long num = q.top();
			q.pop();
			if(num & 1){
				//odd computationally efficient
				q.push(num/2);
				q.push(num/2);

				if(j == K-1){
					cout<<num/2<<" "<<num/2<<endl;
				}
			} else{
				//even
				q.push(num/2);
				q.push(num/2 - 1);
				if(j == K-1){
					cout<<num/2<<" "<<num/2-1<<endl;
				}
			}
		}
	}
	return 0;
}