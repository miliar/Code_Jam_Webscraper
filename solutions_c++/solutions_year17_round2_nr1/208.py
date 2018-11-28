#pragma comment(linker, "/STACK:1000000000")
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <queue>
#include <deque>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <bitset>
#include <memory>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <ctime> 
#include <stack>
#include <iostream>
#include <functional>
#include <fstream>

#define mp make_pair
#define pb push_back

using ll = long long;
using ld = long double;

using namespace std;

void Solve() {
	int d, n;
	cin >> d >> n;
	ld ans = 0;
	for (int i = 0; i < n; i++) {
		int k, m;
		cin >> k >> m;
		ans = max(ans, (ld)(d - k) / (ld)m);
	}
	cout << (ld)d / ans << endl;
}

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(0); cout.setf(ios::fixed); cout.precision(20);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cout << "Case #" << i << ": ";
		Solve();
	}
	return 0;
}