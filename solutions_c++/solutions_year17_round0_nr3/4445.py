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

void Print(ll x) {
	cout << (x - 1) / 2 << " " << (x - 2) / 2 << endl;
}

void Solve() {
	ll n, k;
	cin >> n >> k;
	n++;
	ll c[] = { 1, 0};
	ll nc[2];
	while (k != 0) {
		nc[0] = nc[1] = 0;
		for (int i = 1; i >= 0; i--) {
			if (k <= c[i]) {
				k = 0;
				Print(n + i);
				break;
			} else {
				k -= c[i];
				nc[i] += c[i];
				nc[n & 1] += c[i];
			}
		}
		c[0] = nc[0], c[1] = nc[1];
		n /= 2;
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