#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <stdio.h>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <limits> 
#include <queue>
#include <cfloat> 

using namespace std;

pair<long, long> solve(long n, long k);
map<pair<long, long>, pair<long, long> > memo;

int main() {
	int t; // number of test cases
	scanf("%d\n", &t);

	
	for (int i = 0; i < t; i++) {
		long n, k;
		scanf("%ld%ld\n", &n, &k);
		pair<long, long> res = solve(n, k);
		cout << "Case #" << i + 1 << ": " << res.first << " " << res.second << endl;
	}
	return 0;
}

pair<long, long> solve(long n, long k) {
	pair<long, long> key = make_pair(n, k);
	if (memo.count(key))
		return memo[key];
	
	//cout << n << "," << k << endl;
	if (k < 1) 
		return make_pair(numeric_limits<long>::max(), numeric_limits<long>::max());
	if (k == 1) // if one person is left
		return make_pair(n/2, (n-1)/2);
	pair<long, long> r1 = solve(n/2, k/2);
	pair<long, long> r2 = solve((n-1)/2, (k-1)/2);
	
	pair<long, long> res = make_pair(min(r1.first, r2.first), min(r1.second, r2.second));
	memo[key] = res;
	return res;
}