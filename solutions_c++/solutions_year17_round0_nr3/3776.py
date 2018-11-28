#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <forward_list>
#include <list>
#include <vector>
#include <bitset>
#include <chrono>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <deque>
#include <stack>
#include <limits>
#include <algorithm>
#include <numeric>
#include <utility>
#include <random>
#include <complex>
#include <tuple>
#include <functional>

using namespace std;


void solve(long long n, long long k) {
	long long b = (long long)log2(k);
	long long start = (long long)pow(2, b) - 1;
	long long stop = (long long)pow(2, b + 1);
	long long max_s = n / stop;
	long long rem_s = n % stop - stop + 1;
	long long sm_min_start = stop - 1 + rem_s;
	long long min_s = max_s;
	if (k > sm_min_start) min_s--;
	if (k > stop - 1 + sm_min_start - start) max_s--;
	cout << max_s << " " << min_s;
}

int main() {
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		
		long long n, k; cin >> n >> k;
		solve(n, k);
		
		cout << endl;
	}	
}
