#include<iostream>
using namespace std;

bool isTidy (long long N) {

	long long p = 9;

	while (N > 0) {
		if (N % 10 > p) {
			return false;
		}
		p = N % 10;
		N /= 10;
	}

	return true;
}

long long getTidy (long long N) {

	for (long long i=N; i>=1; --i) {
		if (isTidy(i)) {
			return i;
		}
	}
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B_small.out", "w", stdout);

	int T;
	cin >> T;

	for (int t=1; t<=T; ++t) {
		long long N;
		cin >> N;

		cout << "Case #" << t << ": " << getTidy(N) << endl;
	}

	return 0;
}