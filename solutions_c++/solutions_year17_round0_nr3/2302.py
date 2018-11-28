#include <iostream>
#include <cstdlib>
#include <utility>

using namespace std;

pair<long long, long long> max_min(long long gap) {
	return{ gap / 2, (gap - 1) / 2 };
}

pair<long long, long long> solve(long long N, long long K) {
	long long high = N, low = N-1;
	long long n_h = 1, n_l = 0;
	long long persons = 0;

	while (persons * 2 + 1 < K) {
		long long high_, low_, n_h_, n_l_;

		high_ = high / 2;
		low_ = high_ - 1;
		n_h_ = n_h;
		n_l_ = n_l;

		if (high % 2 == 0) {
			n_l_ += n_h + n_l;
		}
		else {
			n_h_ += n_h + n_l;
		}

		high = high_;
		low = low_;
		n_h = n_h_;
		n_l = n_l_;

		persons = persons * 2 + 1;
	}

	long long left = K - persons;
	if (left <= n_h) {
		return max_min(high);
	}
	else {
		return max_min(low);
	}
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		// read input
		long long N, K;
		cin >> N >> K;

		cout << "Case #" << t + 1 << ": ";

		// solution here
		pair<long long, long long> y_z = solve(N, K);
		cout << y_z.first << " " << y_z.second;

		cout << endl;
	}
}