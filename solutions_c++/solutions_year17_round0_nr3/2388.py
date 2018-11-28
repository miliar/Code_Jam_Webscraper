#include <string>
#include <iostream>
#include <utility>
#include <cstdio>
using namespace std;

typedef unsigned long long ull;
typedef pair<ull, ull> pull;

bool is_odd(ull x) {
	return x & 1;
}

 pull f(ull n, ull k) {
	if (k == 1ULL) {
		return pull(n / 2, (n - 1) / 2);
	}

	if (is_odd(n) || !is_odd(k)) {
		return f(n / 2, k / 2);
	} else {
		return f(n / 2 - 1, k / 2);
	}
}

int main()
{
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);

	int tests, caseNumber = 0;
	ull n, k;
	cin >> tests;
	while (++caseNumber <= tests) {
		cin >> n >> k;
		pull answer = f(n, k);
		cout << "Case #" << caseNumber << ": " << answer.first << " " << answer.second << endl;
	}
	return 0;
}
