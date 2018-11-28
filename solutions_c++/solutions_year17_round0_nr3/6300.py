#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> getSpace(int n, int k) {
	priority_queue<int> check;
	vector<int> ret;
	ret.push_back(0);
	ret.push_back(0);
	
	if (k == 1) {
		ret[0] = n/2;
		ret[1] = n-n/2-1;
	}
	int oneside = n/2;
	int otherside = n-n/2-1;
	check.push(oneside);
	check.push(otherside);
	for (int i = 1; i < k; i++) {
		int larger = check.top();
		//cout << larger << endl;
		check.pop();
		if (larger == 1) {
			return ret;
		}
		int oneside = larger/2;
		int otherside = larger-larger/2-1;
		if (i == k-1) {
			ret[0] = oneside;
			ret[1] = otherside;
		}
		check.push(oneside);
		check.push(otherside);	
	}
	sort(ret.rbegin(), ret.rend());
	return ret;                                                                                                                                                                     
}

int main(int argc, char *argv[]) {
	int t, k, n;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> k >> n;
		vector<int> ret = getSpace(k,n);	
		//int min_space = ret[0];
		//int max_space = ret[1];
		
		cout << "Case #" << i << ": " <<ret[0] << " " << ret[1]<< endl;
	}
}