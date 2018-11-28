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
	int n, R, O, Y, G, B, V;
	cin >> n >> R >> O >> Y >> G >> B >> V;
	vector<pair<int, char> > v;
	v.push_back({R, 'R'});
	v.push_back({B, 'B'});
	v.push_back({Y, 'Y'});

	sort(v.begin(), v.end());
	if(v[2].first > v[0].first + v[1].first){
		cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
		return;
	}

	cout << "Case #" << t + 1 << ": ";
	while(v[2].first > 0){
	//	cout <<endl<< v[0].first << " " << v[0].second << " " << v[1].first << " " << v[1].second << " " << v[2].first << " " << v[2].second << " "<< endl;
		cout << v[2].second;
		if(v[1].first != 0) cout << v[1].second;
		v[2].first --;
		v[1].first --;
		if(v[0].first >= v[1].first) swap(v[0], v[1]);
	}

	v.pop_back();

//	cout << "**";	

	while(v[1].first > 0){
	//	cout <<endl<< v[0].first << " " << v[0].second << " " << v[1].first << " " << v[1].second << " " << v[2].first << " " << v[2].second << " "<< endl;
		cout << v[1].second;
		if(v[0].first != 0) cout << v[0].second;
		v[1].first --;
		v[0].first --;
	//	if(v[0].first > v[1].first) swap(v[0], v[1]);
	}


	cout << endl;
	return;
}

int main(){
	int T;
	cin >> T;
	For(i, T) solve(i);
	return 0;
}
