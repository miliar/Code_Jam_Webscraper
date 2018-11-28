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

void solve(int T){
	int k, res = 0;
	string s;
	bool p = false, isOk = true;
	cin >> s >> k;
	vector<int> pos(s.length(), 0),v;
	v = pos;
	For(i, s.length()) if(s[i] == '+') v[i] = true;
	For(i, s.length()){
		p ^= pos[i];
	//	cout << "i = " << i << "   p = " << p << endl;
		if(i > s.length() - k){
			if(v[i] ^ p == 0){
				isOk = false;
	//			cout << " * ";
			}
			continue;
		}
		if(v[i] ^ p == false){
			res++;
			p = !p;
			if(i + k < s.length()) pos[i+k] = !pos[i+k];
		}
	}
	if(isOk) cout << "Case #" <<  T +1<< ": " << res << endl;
	else cout << "Case #" << T +1<< ": IMPOSSIBLE" << endl;

}

int main(){
	int T;
	cin >> T;
	For(i, T) solve(i);
	return 0;
}
