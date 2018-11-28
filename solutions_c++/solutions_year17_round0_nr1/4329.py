#pragma comment(linker, "/STACK:1000000000")
#define _CRT_SECURE_NO_WARNINGS
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

#define mp make_pair
#define pb push_back

using ll = long long;
using ld = long double;

using namespace std;

const int MAXN = 2001;
int a[MAXN];
void Solve() {
	string s;
	cin >> s;
	int k;
	cin >> k;
	int n = s.length();
	for (int i = 0; i < n; i++) {
		a[i] = (s[i] != '+');
	}
	int ans = 0;
	for (int i = 0; i + k <= n; i++) {
		if (a[i]) {
			for (int j = i; j < i + k; j++)
				a[j] ^= 1;
			ans++;
		}
	}
	for (int i = 0; i < n; i++) 
		if (a[i]) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	cout << ans << endl;
}

int main()
{
	ios_base::sync_with_stdio(0);
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; cas++) {
		cout << "Case #" << cas << ": ";
		Solve();
	}
	return 0;
}