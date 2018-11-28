#include <stdio.h>
#include <algorithm>
#include <string>
#include <queue>
#include <map>
#include <tuple>
#include <iostream>

using namespace std;

typedef long long LL;

void solve(LL n, LL k) {
	LL c;
	map<LL,LL> q;
	q.emplace(n, 1);
	while (k > 0) {
		tie(n, c) = *--q.end();
		if (n == 0)
			throw 42;
		q.erase(n);
		LL Ls = (n - 1) / 2;
		LL Rs = n / 2;
		if (c >= k) {
			cout << Rs << " " << Ls;
			return;
		}
		k -= c;
		q[Ls] += c;
		q[Rs] += c;
	}
	throw 42;
}

#define DIR "C:/Users/dmarin3/Downloads/"
#define PROBLEM "C"
#define ATTEMPT "0"

#define LARGE
//#define TEST

int main() {
#ifdef LARGE
	freopen(DIR PROBLEM "-large.in", "rt", stdin);
#elif defined(TEST)
	freopen("input.txt", "rt", stdin);
#else
	freopen(DIR PROBLEM "-small-2-attempt" ATTEMPT ".in", "rt", stdin);
#endif
	freopen("output.txt", "wt", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		long long n, k;
		cin >> n >> k;
		cout << "Case #" << (i + 1) << ": ";
		solve(n, k);
		cout << endl;
	}
}
