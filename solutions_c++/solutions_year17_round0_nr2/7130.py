#include <cstring>
#include <iostream>
#include <cmath>

using namespace std;

const long long BIG = -2e18;
const int MAX_DIG = 9;
const int MIN_DIG = 0;
const int N = 20;

class Solution {

long long f[22][10][2];
int a[22];
long long mul[22];

public:

	void reset() {
		memset(f, 0, sizeof(f));
	}

	void init(long long n) {
		for(int i = 0; i < N; i++) {
			a[i] = n % 10;
			n /= 10;
		}
	}

	long long calculate(long long n) {
		long long res = 0, sum = 0;
		for(int i = N - 2; i >= 0; i--) {
			if (a[i] < a[i + 1]) { break; }
			if (i == 0) { return n; }
			sum += a[i] * mul[i];
			if (a[i] > a[i + 1]) {
				res = max(res, sum - 1);
			}
		}
		return res;
	}

	long long solve(long long n) {
		init(n);
		return calculate(n);
	}

	void execute()  {
		mul[0] = 1;
		for(int i = 1; i <= 18; i++) {
			mul[i] = mul[i - 1] * 10;
		}
		int test = 0;
		cin >> test;
		for(int t = 1; t <= test; t++) {
			long long n;
			cin >> n;
			cout << "Case #" << t << ": " << solve(n) << endl;
		}
	}
};


int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	Solution sol;
	sol.execute();
	return 0;
}