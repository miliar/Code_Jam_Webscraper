//============================================================================
// Name        : C.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <map>
using namespace std;
#define MAXN 2010
#define oo 1e9
#define MOD 1000000007
typedef long long LL;
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		LL n, k;
		cin >> n >> k;
		LL a, b;
		map<LL, LL> mp;
		mp[n] = 1;
		while (true) {
			map<LL, LL>::iterator it = --mp.end();
			LL mid = (it->first + 1) / 2;
			a = mid - 1;
			b = it->first - mid;
//			cout << a << " " << b << endl;
			if (it->second >= k) {
				break;
			}
			if (a) {
				mp[a] += it->second;
			}
			if (b) {
				mp[b] += it->second;
			}
			k -= it->second;
			mp.erase(it);
		}
		printf("Case #%d: %lld %lld\n", t, b, a);
	}
	return 0;
}
