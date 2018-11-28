#include <cfloat>
#include <climits>
#include <cmath>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

typedef unsigned long long ull;

void run(
	ull gaps,
	ull persons,
	ull& max_out,
	ull& min_out)
{
	gaps -= 1;
	min_out = gaps >> 1;
	max_out = gaps - min_out;
	ull num_big = (max_out > min_out) ? 1 : 0;
	ull num_small = (max_out > min_out) ? 1 : 2;
	ull num_big_big = 0;
	ull num_big_small = (max_out > min_out) ? 1 : 0;

	ull power = 1;
	while (persons > power) {
		persons -= power;
		power <<= 1;

		min_out -= 1;
		max_out -= 1;

		ull min_min = min_out >> 1;
		ull min_max = min_out - min_min;
		min_out = min_min;

		ull max_min = max_out >> 1;
		ull max_max = max_out - max_min;
		max_out = max_max;

		if (min_min < min_max) {
			num_big_small = num_small;
			num_big_big = num_big;
			num_big += num_big;
			num_big += num_small;
		} else if (max_min < max_max) {
			num_big_small = num_big;
			num_big_big = 0;
			num_small += num_small;
			num_small += num_big;
		} else if (max_max == min_min) {
			num_big_small = 0;
			num_big_big = 0;
			num_small = (num_small+num_big) << 1;
			num_big = 0;
		} 
	}

	if (persons <= num_big_big) {
		min_out = max_out;
		return;
	}
	persons -= num_big_big;
	if (persons <= num_big_small) {
		return;
	}
	//persons in num_small_small range
	max_out = min_out;
	return;
}

void test() {
	ull N, K;
	cin >> N >> K;

	ull A = 0, B = 0;

	run(N,K,A,B);

	cout << A << ' ' << B;
}	

int main() {
	int T;
	cin >> T;
	for(int i = 1; i<=T; i++) {
		cout << "Case #" << i << ": ";
		test();	
		cout << endl;
	}
	return 0;
}
