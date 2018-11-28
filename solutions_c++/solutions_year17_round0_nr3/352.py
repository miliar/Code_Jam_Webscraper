#include <iostream>
#include <fstream>
#include <stdio.h>

#include <string>
#include <map>
#include <utility>
#include <algorithm>


using namespace std;

pair<long long, long long> solve(long long n, long long k) {
	if (n == k) return make_pair(0,0);
	//else if (k == n-1) return make_pair(0,1);


	if (n % 2 == 1) {
		if (k == 1) return make_pair(n/2, n/2);
		k--;

		return solve(n/2, k/2+k%2);
	}
	else {
		if (k == 1) return make_pair(n/2-1, n/2);
		k--;
		if (k % 2 == 1) return solve(n/2, k/2+1);
		else return solve(n/2-1, k/2);
	};
};


int main() {
	int t;
	cin >> t;
	for (int i0 = 1; i0 <= t; ++i0) {
		long long n, k;
		cin >> n >> k;
		auto p = solve(n, k);
		printf("Case #%d: %lld %lld\n", i0, p.second, p.first);
		
	};

}