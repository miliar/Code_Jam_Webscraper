#pragma comment(linker, "/STACK:500000000")
#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <assert.h>
#include <bitset>
#include <exception>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <math.h>
#include <set>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
const double PI = acos(-1.0);
const double EPS = 1e-9;
const int INF = static_cast<int>(2e9);

char s[29];

bool check(int v) {
	int minV = 9;
	while (v > 0) {
		if (v % 10 > minV) {
			return false;
		}
		minV = min(minV, v % 10);
		v /= 10;
	}
	return true;
}

int brute(int n) {
	while (!check(n)) {
		--n;
	}
	return n;
}

string getNines(int len) {
	string res = "";
	for (int i = 0; i < len; ++i) {
		res += '9';
	}
	return res;
}

int main() {
	freopen("1.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: %d\n", tt, brute(n));
		/*scanf("%s", s);
		int n = strlen(s);
		string res = "";
		printf("Case #%d: ", tt);
		for (int i = 0; i < n; ++i) {
			int minV = INF;
			for (int j = i; j < n; ++j) {
				minV = min(minV, (int) (s[j] - '0'));
			}
			if (minV < s[i] - '0') {
				if (s[i] == '1') {
					res = getNines(n);
					break;
				}
				res += s[i] - 1;
				res += getNines(n - 1 - i);
				break;
			}
			res += s[i];
		}
		printf("%s\n", res.c_str());*/
	}
	return 0;
}