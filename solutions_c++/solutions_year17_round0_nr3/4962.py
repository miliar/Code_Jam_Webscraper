#include <algorithm>
#include <functional>
#include <queue>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

int main(){
	int cases;
	cin>>cases;

	for (int cas=1; cas<=cases; ++cas){
		cout << "Case #"<<cas << ": ";

		int K,N;

		cin>>N>>K;

		priority_queue<int> que;

		que.push(N);

		for (int i=0;i<K-1;++i){
			int tmp=que.top();
			que.pop();

			tmp-=1;

			que.push(tmp/2);
			que.push((tmp+1)/2);
		}

		int t = que.top();

		cout << t/2 << " " << (t-1)/2 << endl;
	}
}
