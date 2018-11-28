#define _CRT_SECURE_NO_WARNINGS


#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <unordered_map> //C++11
using namespace std;

typedef long long ll;

int t;
ll n, k, p2, quot, rem;

int p(ll n);

int main() {
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> n >> k;
		p2 = pow(2, p(k));
		quot = (n - p2 + 1) / p2;
		rem = (n - p2 + 1) % p2;
		if (k - p2 + 1 <= rem) n = quot + 1;
		else n = quot;
		if ((n - 1) % 2 == 0) cout << "Case #" << i << ": " << (n - 1) / 2 << " " << (n - 1) / 2 << endl;
		else cout << "Case #" << i << ": " << (n - 1)/2 + 1 << " " << (n - 1)/2 << endl;
	}
	return 0;
}

int p(ll n) {
	if (n/2 == 0) return 0;
	return p(n / 2) + 1;
}