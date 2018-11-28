#include <iostream>
using namespace std;

typedef unsigned long long ull;
const ull one = 1;

ull n, k;

ull power_of(int e) {
	return one << e;
}

int exponent_of_power_less_than_or_equal(ull k) {
	int e = 0;
	while (power_of(e + 1) <= k)
		e++;
	return e;
}

int main() {
	int cases;
	cin >> cases;
	for (int case_counter = 1; case_counter <= cases; case_counter++) {
		cin >> n >> k;

		int level = exponent_of_power_less_than_or_equal(k);
		//cout << "level  " << level << endl;

		ull nodes_in_level = power_of(level);
		//cout << "nodes_in_level  " << nodes_in_level << endl;

		ull bathrooms_taken = nodes_in_level - 1;
		//cout << "bathrooms_taken  " << bathrooms_taken << endl;

		ull bathrooms_left = n - bathrooms_taken;
		//cout << "bathrooms_left  " << bathrooms_left << endl;

		ull in_each = bathrooms_left / nodes_in_level;
		//cout << "in_each  " << in_each << endl;

		ull nodes_with_one_more = bathrooms_left % nodes_in_level;
		//cout << "nodes_with_one_more  " << nodes_with_one_more << endl;

		ull bathrooms_left_to_take = k - bathrooms_taken;
		ull to_split = bathrooms_left_to_take <= nodes_with_one_more ? in_each : in_each - 1;
		ull min = to_split / 2;
		ull max = min + (to_split % 2);

		cout << "Case #" << case_counter << ": " << max << " " << min << endl;
	}
	return 0;
}
