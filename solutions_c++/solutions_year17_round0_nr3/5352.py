#include <iostream>
#include<vector>
#include<algorithm>
#include <queue>
using namespace std;

class Comparing{
	public:
	bool operator()(pair<int,int> a,pair<int,int> b) {
        if(a.second-a.first==b.second-b.first)
			return a.first>b.first;
		return a.second-a.first<b.second-b.first;
    }
};

pair <int, int> fun (int n, int k){
	pair <int, int> result (0,0);
	if(n == k)
		return result;

		
	priority_queue <pair<int, int>, vector<pair<int, int>>, Comparing> myQueue;
	
	myQueue.emplace(pair<int,int>(0,n+1));
	
	for(int i=1;i<k;++i){
		pair <int, int> split  (myQueue.top().first, myQueue.top().first+(myQueue.top().second-myQueue.top().first)/2);
		pair <int, int> split2 (myQueue.top().first+(myQueue.top().second-myQueue.top().first)/2,myQueue.top().second);
		myQueue.pop();
		myQueue.emplace(split);
		myQueue.emplace(split2);
	}
	
	int right = myQueue.top().first;
	int left =  myQueue.top().second;
	
	(right+left)/2 - right> left - (right+left)/2?result = pair<int, int>(((right+left)/2 - right)-1,(left - (right+left)/2)-1):result =pair<int, int>((left - (right+left)/2)-1,((right+left)/2 - right)-1);

	return result;
}

int main() {
	int amount = 0;
	int n = 0;
	int k = 0;
	
	cin >> amount;
	
	for(int i=0;i<amount;++i){
		cin >> n >> k;
		pair<int, int> result = fun(n, k);
		cout << "Case #" << i+1 << ": " << result.first << " " << result.second<< endl;
	}
	
	
	return 0;
}