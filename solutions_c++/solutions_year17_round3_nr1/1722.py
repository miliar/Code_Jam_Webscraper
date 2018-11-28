#include<iostream>
#include<vector>
#include<set>
#include<unordered_set>
#include<unordered_map>
#include<map>
#include<cmath>
#include<string>
#include<algorithm>
#include<string.h>
#include<utility>
#include<queue>
#include<stack>
using namespace std;
long long solve(int ind, int left, vector<vector<long long> >& result, vector<pair<long long,long long> >& inp){
	if (left == 0)
		return 0;
	if (left == 1)
		return 2*inp[ind].first*inp[ind].second;
	if (ind >= inp.size()){
		return -1000000000000000000;
	}
	if (result[ind][left] != -1)
		return result[ind][left];
	
	result[ind][left] = -1000000000000000000;
	for (int i = ind + 1; i < inp.size(); ++ i){
		result[ind][left] = max(result[ind][left], solve(i, left - 1, result, inp));
	}
	if (result[ind][left] > 0)
		result[ind][left] += 2*inp[ind].first*inp[ind].second;
	return result[ind][left];
}
int main(){
	int t, h, r;
	cin >> t;
	for (int z = 1; z <= t; ++ z){
		int n, k;
		cin >> n >> k;
		vector<vector<long long> > result(n+1, vector<long long>(k+1, -1));
		vector<pair<long long,long long> > inp;
		for(int i = 0; i < n; ++ i){
			cin >> r >> h;
			inp.push_back(pair<long long,long long>(r, h));
		}
		sort(inp.begin(), inp.end());
		reverse(inp.begin(), inp.end());
		long long mx = 0;
		for (int i = 0; i < inp.size(); ++ i){
			long long val = solve(i, k, result, inp);
			if (val < 0) continue;
			mx = max(mx, val + inp[i].first*inp[i].first);
			//cout << mx << endl;
		}
		double vv = mx;
		printf("Case #%d: %.12f\n", z, vv*3.1415926535897932);
	}
	return 0;
}