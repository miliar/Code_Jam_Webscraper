#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <iomanip>
#include <utility>
#include <stack>
#include <memory.h>
#include <ctime>
#include <cstdlib>
#include <sstream>
#include <unordered_set>
#include <unordered_map>
#include <cstring>
#include <inttypes.h>

#define FILE "B-large"
#define fi first
#define se second
#define pb push_back
#define matrix(type) vector<vector<type>>
#define sqr(x) ((x)*(x))
using namespace std;

typedef long long LL;
typedef long double LD;

const int INF = 2e9;
const LD PI = 3.14159265358979323846;
const LD EPS = 1e-10;
const int MOD = 1e9 + 7;

const int N = 1e8 + 10;
const int M = 1e5 + 10;

string solve(string &s){
	bool move = true;
	int  l = s.length();
	for (int i = l - 2; i+1; --i) {
		if (s[i] > s[i+1]) {	
			s[i]--;
			for (int j = i + 1; j < l; ++j) s[j] = '9';
		}
	}
	while (s[0] == '0') s.erase(0,1);
	return s;
}

int main() {
	ios_base::sync_with_stdio(false);
	freopen(FILE".in", "r", stdin); freopen(FILE".out", "w", stdout);
	int t;
	string s;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> s;
		cout << "Case #" << i << ": " << solve(s) << endl;
	}
	return 0;
}