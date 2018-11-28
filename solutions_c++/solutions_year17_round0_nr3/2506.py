#include <algorithm>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#define SREP(s,i,m) for(unsigned int i = s; i < m; ++i)
#define REP(i,m) SREP(0,i,m)

using namespace std;

#ifdef _MSC_VER
using LONG = __int64;
using ULONG = unsigned __int64;
#else
using LONG = long long int;
using ULONG = unsigned long long int;
#endif

void solve(LONG n, LONG k) {
	LONG left_n = (n - 1) / 2;
	LONG right_n = n / 2;
	LONG next_k = k / 2;
	if (k == 1) {
		LONG max = n / 2;
		LONG min = (n - 1) / 2;
		cout << max << " " << min << endl;
		return;
	}
	// ‹ô”‚Å-1, Šï”‚Å1
	int n_sign = (n % 2) * 2 - 1;
	int k_sign = (k % 2) * 2 - 1;
	if (n_sign * k_sign > 0) {
		solve(right_n, next_k);
	}
	else {
		solve(left_n, next_k);
	}
	//if (n % 2 == 0) {
	//	if (k % 2 == 0) {
	//		solve(right_n, next_k);
	//	}
	//	else {
	//		solve(left_n, next_k);
	//	}
	//}
	//else {
	//	if (k % 2 == 0) {
	//		solve(left_n, next_k);
	//	}
	//	else {
	//		solve(right_n, next_k);
	//	}
	//}
}

int main(void) {
	int T;
	cin >> T;
	REP(i, T) {
		LONG N, K;
		cin >> N >> K;
		cout << "Case #" << (i + 1) << ": ";
		solve(N, K);
	}
	return 0;
}