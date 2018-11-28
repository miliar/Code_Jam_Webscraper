#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <cmath>
#include <string>
#include <set>
#include <deque>
#include <cctype>
#include <bitset>
#include <regex>

using namespace std;

#define For(i, n) for(int (i) = 0; (i) < (n); (i)++)

void solve(int t){
	int n, q;
	cin >> n >> q;
	vector<pair<long double,long double> > info(n);
	For(i, n) cin >> info[i].first >> info[i].second;
	vector<vector<long double> > v(n, vector<long double> (n));
	For(i, n){
		For(j, n){
			cin >> v[i][j]; 
		}
	}

	//for(auto x: info) cout << x.first << " " << x.second << endl;

	vector<long double> best(n, -1);
	best[0] = 0;
	For(i, n-1){
		long double speed = info[i].second;
		long double dist = info[i].first;
		long double to = 0;
		int k = i;
	//	cout << "i: " <<i << endl;
		while(k < n && to <= dist){
	//		cout << "to: " << to << endl;
			if(best[k] != -1) best[k] = min(best[k], best[i] + to/speed);
			else best[k] = best[i] + to/speed;
			to += v[k][k+1];
			k++;
		}

	//	cout << "best: "; for(auto x: best) cout << x << " "; cout << endl;
	}

	long double x;
	cin >> x >> x;

	printf("Case #%d: %.8Lf\n", t+1, best.back());
	return;
}

int main(){
	int T;
	cin >> T;
	For(i, T) solve(i);
	return 0;
}
