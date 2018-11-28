#include<iostream>
#include<queue>
#include<vector>
using namespace std;

pair<int, int> calc(int n, int k) {
	int ansmx = 0, ansmn = n;
	auto cmp = [](int left, int right) {
		return left < right;
	};
	priority_queue<int, vector<int>, decltype(cmp)> que(cmp);
	que.push(n);
	for(int i=0;i<k;i++) {
		auto tp = que.top();que.pop();
		int rs = tp/2;
		int ls = rs;
		if (tp%2==0) {
			ls--;
		}
		ansmx = rs;
		ansmn = ls;
		if (ansmx) {
			que.push(ansmx);
		}
		if (ansmn) {
			que.push(ansmn);
		}
	}
	return pair<int, int> {ansmx, ansmn};
}

int main() {
	int T;
	cin>>T;
	for(int t=1;t<=T;t++) {
		int n, k;
		cin>>n>>k;
		auto res = calc(n, k);
		cout<<"Case #"<<t<<": "<<res.first<<" "<<res.second<<endl;
	}
	return 0;
}
