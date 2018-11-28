#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <cmath>
#include <string>
using namespace std;

void solve(int N, int K) {
	//vector<int> maxset; 
	map<int, int> maxmap;
	
	int lmx, rmx, mx;
	
	if(N==K) {
		cout << "0 0" << endl;
		return;
	}
	
	
	//maxset.push_back(N);
	maxmap[N] = 1;
	
	for(int i=1; i<=K; i++) {
		map<int,int>::iterator it = max_element(maxmap.begin(), maxmap.end());
		pair<int, int> mxpair = *it;
	
		//cout << mxpair.first << " " << mxpair.second << endl;	
		int mx = mxpair.first;
		if(mx%2==0) {
			lmx = mx/2-1;
			rmx = mx/2;
		}
		else {
			lmx = rmx = mx/2;
		}
		
		maxmap[mx] = maxmap[mx] - 1;
		if(maxmap[mx]==0) {
			maxmap.erase(mx);
		}
		
		if(maxmap.find(lmx) != maxmap.end()) {
			maxmap[lmx] = maxmap[lmx] + 1;
		}
		else {
			maxmap[lmx] = 1;
		}
		
		if(maxmap.find(rmx) != maxmap.end()) {
			maxmap[rmx] = maxmap[rmx] + 1;
		}
		else {
			maxmap[rmx] = 1;
		}
		//maxset.erase(it);
		//maxset.push_back(lmx);
		//maxset.push_back(rmx);
		
		//cout << mx << " : " << lmx << " - " << rmx << endl;
		//cout << "Array: ";
		//for(int j=0; j<maxset.size(); ++j) {
			//cout << maxset[j] << " ";
		//}
		//cout << endl;
		
	}
	
	cout << max(lmx,rmx) << " " << min(lmx,rmx) << endl;
}


int main() {
	int T;
	cin >> T;
	
	int N, K;
	for(int t=1; t<=T; ++t) {
		cin >> N >> K;
		cout << "Case #" << t << ": ";
		solve(N, K);
	}
	return 0;
}