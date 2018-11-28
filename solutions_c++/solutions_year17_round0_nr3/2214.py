#include <cstdio>
#include <cstring>
#include <utility>
using namespace std;

pair<long long, long long> solve(long long number[2], long long count[2], long long K) {
	// printf(" [[[[]]]] {%lld %lld} {%lld %lld} %lld\n", number[0], number[1], count[0], count[1], K);
	long long newK = K - count[0] - (count[1] > 0 ? count[1] : 0);
	if (newK <= 0) {
		if (K - count[0] <= 0) return make_pair(number[0] / 2, (number[0] - 1) / 2);
		else return make_pair(number[1] / 2, (number[1] - 1) / 2);
	}
	long long new_number[2] = {-1, -1};
	long long new_count[2] = {0, 0};
	for (int i = 0; i < 2; i++) {
		if (number[i] < 0) break;
		bool flag = false;
		for (int j = 0; j < 2; j++) {
			if (number[i] / 2 == new_number[j]) {
				flag = true;
				new_count[j] += count[i];
				break;
			}
		}
		if (!flag) {
			int newP = new_number[0] < 0 ? 0: 1;
			new_number[newP] = number[i] / 2;
			new_count[newP] = count[i];
		}

		flag = false;
		for (int j = 0; j < 2; j++) {
			if ((number[i] - 1) / 2 == new_number[j]) {
				flag = true;
				new_count[j] += count[i];
				break;
			}
		}
		if (!flag) {
			int newP = new_number[0] < 0 ? 0: 1;
			new_number[newP] = (number[i] - 1) / 2;
			new_count[newP] = count[i];
		}
	}
	return solve(new_number, new_count, newK);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int caseN = 1; caseN <= T; caseN++) {
		long long n, K;

		scanf("%lld%lld", &n, &K);
		long long number[2] = {n, -1};
		long long count[2] = {1, -1};
		pair<long long, long long> ans = solve(number, count, K);

		printf("Case #%d: %lld %lld\n", caseN, ans.first, ans.second);
	}

	return 0;
}