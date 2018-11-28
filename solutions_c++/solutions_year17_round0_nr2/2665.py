#include <bits/stdc++.h>

#define FOR(i, start, end) for (int i = start; i < end; ++i)
#define RFOR(i, start, end) for (int i = end - 1; i >= start; --i)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int T;
ull N;

vector<int> to_digits(ull number, ull base) {
	vector<int> result;
	while (number) {
		ull next = number / base;
		result.push_back(number - (next * base));
		number = next;
	}
	return result;
}

void print_digits(vector<int> digits) {
	bool leading_zero = true;
	RFOR(i, 0, digits.size()) {
		int digit = digits[i];
		if (digit != 0 || !leading_zero) {
			leading_zero = false;
			printf("%d", digit);
		}
	}
}

bool finished(vector<int> digits) {
	FOR(i, 1, digits.size()) {
		if (digits[i] > digits[i - 1]) return false;
	}
	return true;
}

int main()
{
	// freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("qr_b.out", "w", stdout);
	scanf("%d", &T);
	FOR(t, 1, T + 1) {
		printf("Case #%d: ", t);
		scanf("%llu", &N);

		vector<int> digits = to_digits(N, 10);
		
		while (!finished(digits)) {
			RFOR(i, 1, digits.size()) {
				if (digits[i] > digits[i - 1]) {
					FOR(j, 0, i) {
						digits[j] = 9;
					}
					digits[i]--;
				}
			}
		}
		
		print_digits(digits);
		printf("\n");
	}
	return 0;
}
