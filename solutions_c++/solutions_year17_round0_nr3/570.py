#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <cstdio>
#include <set>
#include <cstring>
using namespace std;

void report(long long n) {
	n--;
	long long l = n>>1;
	long long r = n - l;
	cout << r << " " << l;
}

void solve() {
	long long n;
	long long k;
	cin >> n >> k;
	long long c0 = 1, c1 = 0;
	while (1) {
		if (k <= c0+c1) { // get answer immediately
			if (k <= c1) {
				report(n+1);
				return;
			}
			else {
				report(n);
				return;
			}
		}
		k -= (c0+c1);
		long long n0 = (n-1) >> 1;
		long long n1 = n0+1;
		long long d0 = 0, d1 = 0;
		long long t1 = (n-1) >> 1;
		long long t2 = (n-1) - t1;
		long long t3 = (n) >> 1;
		long long t4 = (n)-t3;
		if (t1 == n0) d0 += c0;
		if (t2 == n0) d0 += c0;
		if (t3 == n0) d0 += c1;
		if (t4 == n0) d0 += c1;
		if (t1 == n1) d1 += c0;
		if (t2 == n1) d1 += c0;
		if (t3 == n1) d1 += c1;
		if (t4 == n1) d1 += c1;
		
		c0 = d0;
		c1 = d1;
		n = n0;
	}
}

int main(int argc, char *argv[]) {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int testNum;
	cin >> testNum;
	for (int testid = 0; testid < testNum; ++testid ) {
		cout << "Case #" << testid+1 << ": ";
		solve();
		cout << endl;
	}
}