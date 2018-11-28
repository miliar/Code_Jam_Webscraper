#include <cstdio>
#include <cstring>
#include <cstdint>
#include <cinttypes>
#include <cassert>
#include <map>
#include <iostream>

using namespace std;

void compute_categories(int64_t n, map<int64_t, int64_t> &cats) {
	map<int64_t, int64_t> unexpanded_cats;
	unexpanded_cats[n] = 1;
	while (!unexpanded_cats.empty()) {
		auto i = unexpanded_cats.begin();
		cats[i->first] += i->second;
		if (i->first > 0) {
			int n_left = i->first - 1;
			unexpanded_cats[n_left / 2] += i->second;
			unexpanded_cats[n_left - n_left / 2] += i->second;
		}
		unexpanded_cats.erase(i);
	}

}

/*void aux(int n_rounds, int64_t n, int64_t k, int64_t *min, int64_t *max) {
	*min = (n - 1) / 2;
	*max = *min + (n - 1) % 2;
	if (n_rounds == 0)
		return;	
	assert(n > 0);
	assert(k > 0);
	//int smaller = (n_rounds % 2) ^ (((k >> (n_rounds - 1)) % 2)? 0 : 1);
	int smaller = (k >> (n_rounds - 1)) % 2;
	n--;
	n = (n / 2) + (smaller? 0 : (n % 2));
	printf("n=%"PRIi64" k=%"PRIi64"\n", n, k);
	aux(n_rounds - 1, n, k, min, max);
}*/

void solve_test_case(int c, int64_t n, int64_t k) {
	int64_t min = 0, max = 0;
	map<int64_t, int64_t> cats;
	compute_categories(n, cats);
	for (auto i = cats.rbegin(); i != cats.rend(); i++) {
		//cout << i->first << ": " << i->second << endl;
		if (k <= i->second) {
			min = (i->first - 1) / 2;
			max = (i->first - 1) - min;
			break;
		}
		k -= i->second;
	}
	printf("Case #%d: %" PRIi64 " %" PRIi64 "\n", c, max, min);
}

int main(void) {
	int n_test_cases;
	scanf("%d", &n_test_cases);
	for (int i = 0; i < n_test_cases; ++i) {
		int64_t k, n;
		scanf("%" SCNi64 "%" SCNi64, &n, &k);
		solve_test_case(i+1, n, k);
	}
	return 0;
}
