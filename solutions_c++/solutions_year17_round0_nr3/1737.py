#include<iostream>
#include<string>
#include<vector>

using namespace std;

int logBaseTwo(long long n) {
	int i = -1;
	long long k = 1;
	while (k <= n) {
		k *= 2;
		++i;
	}
	return i;
}

long long power(long long n, int k) {
	long long N = 1;
	for (int i = 0; i < k; ++i) {
		N *= n;
	}
	return N;
}

long long makeStep(long long n, long long& x, long long& y) {
	if (n % 2 == 0) y = x + 2 * y;
	else x = 2 * x + y;
	return (n - 1) / 2;
}

void solve(long long N, long long K, long long& minDistance, long long& maxDistance) {
	int numberOfSteps = logBaseTwo(K);
	long long x = 1;
	long long y = 0;
	long long n = N;
	for (int i = 0; i < numberOfSteps; ++i) {
		n = makeStep(n, x, y);
	}
	if (K - power(2, numberOfSteps) < y) {
		minDistance = n / 2;
		maxDistance = (n + 1) / 2;
	}
	else {
		minDistance = (n - 1) / 2;
		maxDistance = n / 2;
	}
	return;
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; ++i) {
		long long N, K, minDistance, maxDistance = 0;
		cin >> N >> K;
		solve(N, K, minDistance, maxDistance);
		cout << "case #" << i << ": " << maxDistance << ' ' << minDistance << '\n';
	}
	
	
}