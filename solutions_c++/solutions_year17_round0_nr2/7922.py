#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>

using namespace std;

bool isTidyNumber (long long n) {
	vector<int> nums;
	while (n) {
		nums.push_back(n % 10);
		n /= 10;
	}
	for (int i = 1; i < nums.size(); i++) {
		if (nums[i - 1] < nums[i])
			return false;
	}
	return true;
}

long long stupidWay (long long n) {
	for (long long p = n; p >= 1; --p) {
		if (isTidyNumber(p))
			return p;
	}
	return -1ll;
}

long long getLastTidyNumberUpTo (long long n) {

	vector<int> nums;

	long long temp = n;

	while (n) {
		nums.push_back(n % 10);
		n /= 10;
	}

	reverse(nums.begin(), nums.end());

	n = temp;

	int k = 0;

	for (int i = 1; i < nums.size(); i++) {
		if (nums[i - 1] > nums[i]) {
			k = i;
			break;
		}
	}

	if (k == 0) {
		return n;
	}

	for (int i = k - 1; i >= 0; i--) {
		if (i == 0 || nums[i] - 1 >= nums[i - 1]) {
			--nums[i];
			for (int j = i + 1; j < nums.size(); j++)
				nums[j] = 9;
			break;
		}
	}

	long long res = 0ll;

	for (int i = 0; i < nums.size(); i++)
		res = res * 10ll + nums[i];

	return res;

}

int main () {


	int test;
	cin >> test;
	int cnt = 0;
	while (test--) {

		long long n;
		cin >> n;

		cout << "Case #" << ++cnt << ": " << getLastTidyNumberUpTo(n);

		if (test)
			cout << "\n";

	}


	return 0;

}