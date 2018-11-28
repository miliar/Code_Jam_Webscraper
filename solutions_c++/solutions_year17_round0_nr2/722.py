#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <cfloat>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>

#define MOD 1000000007
#define PI 3.14159265359
#define REP(i,n) for(int i = 0; i < n; ++i)
#define FOR(i,n,m) for(int i = n; i < m; ++i)
#define ll long long

using namespace std;


void func(string  &s) {
	for (int idx = s.size()-2; idx >= 0; --idx) {
		if (s[idx] > s[idx+1]) {
			for (int j = idx+1; j < s.size(); ++j)
				s[j] = '9';
			--s[idx];
		}
	}
	s = s.substr(s.find_first_not_of('0'));
}

int main() {
	int t;
	string str;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> str;
		func(str);
		cout << "Case #" << i << ": " << str << endl;
	}
	return 0;
}
