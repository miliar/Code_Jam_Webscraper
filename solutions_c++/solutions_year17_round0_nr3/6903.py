#include<iostream>
#include<utility>
#include<tuple>
#include<set>
#include<queue>
#include<algorithm>
using namespace std;
int main() {
	int T;
	cin >> T;
	for(int t=1;t<=T;t++) {
		int k,n;
		cin >> n >> k;
		vector<tuple<bool,int,int>>stalls;
		stalls.emplace_back(make_tuple(true, 0,0));
		for(int i=1;i<=n;i++){ 
			stalls.emplace_back(make_tuple(false,i-1, n-i));
		}
		stalls.emplace_back(make_tuple(true, 0, 0));
		auto comp = [&stalls](int a, int b) { return min(get<1>(stalls[a]),get<2>(stalls[a])) < min(get<1>(stalls[b]), get<2>(stalls[b]));}; 
		auto comp2 = [&stalls](int a, int b) { 
			if( max(get<1>(stalls[a]),get<2>(stalls[a])) < max(get<1>(stalls[b]), get<2>(stalls[b]))) {
				return true;
			} else if(max(get<1>(stalls[a]),get<2>(stalls[a])) == max(get<1>(stalls[b]), get<2>(stalls[b]))){
				return a > b;
			}
			else {
				return false;
			}
		}; 
		stalls.emplace_back(make_tuple(true,0,0));

		int stall=0;
		for(int i =0;i<k;i++){
			priority_queue<int, vector<int>, decltype(comp)>pq(comp);
			for(int i=1;i<=n;i++) {
				if(!get<0>(stalls[i]))
					pq.push(i);
			}
			int maxmin = pq.top();
			priority_queue<int, vector<int>, decltype(comp2)> maxmax(comp2);
			while(!pq.empty()&&min(get<1>(stalls[pq.top()]), get<2>(stalls[pq.top()]))==min(get<1>(stalls[maxmin]),get<2>(stalls[maxmin]))){
				maxmax.push(pq.top());
				pq.pop();			
			}
			stall = maxmax.top();
			for(int i=1;i<=n;i++) {
				if(i<stall) {
					get<2>(stalls[i]) = min(get<2>(stalls[i]), stall - i-1);
				}
				else if(i>stall) {
					get<1>(stalls[i]) = min(get<1>(stalls[i]), i-stall-1);
				}
				else {
					get<0>(stalls[stall]) = true;
				}
			}
			maxmax.pop();
			while(!maxmax.empty()) {
				pq.push(maxmax.top());
				maxmax.pop();
			}
			
		}
		for(int i=1;i<=n;i++ ){
		}
		cout <<"Case #"<<t<<": ";
		cout << max(get<1>(stalls[stall]),get<2>(stalls[stall])) << " " << min(get<1>(stalls[stall]),get<2>(stalls[stall]))<<endl;
	}
}
