#include <iostream>
#include <vector>

using namespace std;

vector<int> toVector(long long n) {
	if (n == 0) return {};
	vector<int> res = toVector(n/10);
	res.push_back(n%10);
	return res;
}

long long toNumber(const vector<int> &vec) {
	long long res = 0;
	for (int num : vec) {
		res *= 10;
		res += num;
	}
	return res;
}

long long calc(long long n) {
	vector<int> nums = toVector(n);
	int size = nums.size();
	int idx = size;

	for (int i = size-2; i >= 0; --i) {
		if (nums[i] > nums[i+1]) {
			idx = i;
		}
	}

	if (idx != size) {
		while ((idx > 0) && (nums[idx] == nums[idx-1])) {
			--idx;
		}
		nums[idx]--;
		for (int i = idx+1; i < size; ++i) {
			nums[i] = 9;
		}
	}

	return toNumber(nums);
}

int main() {
	int t;
	long long n;

	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

	for (int i = 1; i <= t; ++i) {
		cin >> n;
		cout << "Case #" << i << ": " << calc(n) << endl;
	}

	return 0;
}

