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

#define FILE "A-large"
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

int check(string &s, int n) {
	int res = 0, l = s.length();
	for (int i = 0; i < l; ++i) {
		if (s[i] == '+') continue;
		if (l - i < n) return -1;
		for (int j = i; j < i + n; ++j)
			if (s[j] == '-') s[j] = '+';
			else s[j] = '-';
		res++;
	}
	return res;
}

int main() {
	ios_base::sync_with_stdio(false);
	freopen(FILE".in", "r", stdin); freopen(FILE".out", "w", stdout);
	int t, n;
	string s;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> s >> n;
		n = check(s, n);
		cout << "Case #" << i << ": ";
		if (n < 0) cout << "IMPOSSIBLE\n";
		else cout << n << endl;
	}
	return 0;
}