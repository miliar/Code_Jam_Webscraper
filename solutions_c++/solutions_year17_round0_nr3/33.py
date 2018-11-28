#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <stack>
#include <queue>

using namespace std;



int main() {
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt ++) {
		long long n, k;
		cin >> n >> k;
		long long kk = 1;
		while (kk * 2 <= k) kk *= 2;
		long long sum = n - kk + 1;
		long long a = sum / kk;
		if ((n+1) % kk > k - kk) a ++;
		cout << "Case #" << tt << ": ";
		cout << a / 2 << ' ' << (a-1) / 2 << endl;
	}

	return 0;
}

