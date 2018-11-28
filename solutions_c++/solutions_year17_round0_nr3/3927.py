#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <tuple>
#include <algorithm>
#include <set>
#include <functional>
using namespace std;

#define sz(a) ((int)((a).size()))
#define fi(a,b) for(int i = (a); i < (b); ++i)
#define fj(a,b) for(int j = (a); j < (b); ++j)


void solve() {
	int n, k;
	cin >> n >> k;
	//cout << endl;
	int ansL, ansR;
	multiset<int, std::greater<int>> ints;
	ints.insert(n);
	fi(0, k) {
		auto it = ints.begin();
		ansL = (*it) / 2;
		ansR = ((*it) - 1) / 2;
		ints.erase(it);
		ints.insert(ansL);
		ints.insert(ansR);
		//cout << i << ' ' << ansL << ' ' << ansR << endl;
	}
	cout << max(ansL, ansR) << ' ' << min(ansL, ansR);
}

int main() {
#ifdef MY_DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
#endif
	int nT;
	cin >> nT;
	fi(0, nT) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}