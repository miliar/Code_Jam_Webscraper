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
int ac = 0;

bool Check(ll x) {
	int last = 9;
	while (x) {
		int nv = (x % 10);
		if (nv > last) return false;
		last = nv;
		x /= 10;
	}
	return true;
}

void Solve() {
	ac = 0;
	ll n;
	cin >> n;
	for (int i = n; i >= 1; i--)
		if (Check(i)) {
			cout << i << endl;
			return;
		}
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