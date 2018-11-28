/*AMETHYSTS*/
#pragma comment(linker, "/STACK:1000000000")
#include <cstdio>
#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#include <fstream>
#include <deque>
#include <stack>
#include <climits>
#include <string>
#include <queue>
#include <memory.h>
#include <map>
#include <unordered_map>
//#include "sort.h"

#define ll long long
#define ld double
#define pii pair <int, int>
#define mp make_pair

using namespace std;

const int maxn = (int)1010;
char s[maxn];

bool cmp(pii a, pii b) {
	if (min(a.first, a.second) != min(b.first, b.second)) {
		return min(a.first, a.second) > min(b.first, b.second);
	}

	if (max(a.first, a.second) != max(b.first, b.second)) {
		return max(a.first, a.second) > max(b.first, b.second);
	}

	return a.first < b.first;
}

vector <pii> solve(int n) {
	if (n == 0) {
		vector <pii> a;
		return a;
	}

	if (n == 1) {
		vector <pii> a;
		a.push_back(mp(0, 0));
		return a;
	}

	int pos = (n + 1) / 2;

	vector <pii> a = solve(pos - 1);
	vector <pii> b = solve(n - pos);

	vector <pii> c(n);
	c[0] = mp(pos - 1, n - pos);

	merge(a.begin(), a.end(), b.begin(), b.end(), c.begin() + 1, cmp);

	return c;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;

	cin >> t;

	for (int it = 1; it <= t; it++) {
		printf("Case #%d: ", it);
		int n;

		cin >> n;

		vector <pii> v = solve(n);

		int k;

		scanf("%d", &k);
		k--;

		if (v[k].first < v[k].second) {
			swap(v[k].first, v[k].second);
		}

		cout << v[k].first << ' ' << v[k].second << endl;
	}

	return 0;
}
