#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string> 
#include <tuple>
#include <vector>
#include <queue>  

using namespace std;  // since cin and cout are both in namespace std, this saves some text

char decrease(char x) {
	
	int value = int(x) - '0' - 1;
	return std::to_string(value)[0];
}
std::vector<int> occupiedBy;
std::vector<int> minS;
std::vector<int> maxS;

deque<int> order(long long start, long long end) {
	// divide step -> calculate order and min/max
	if (start > end) {
		return{};
	}

	// default/break case
	if (start == end) {
		minS[start] = 0;
		maxS[start] = 0;
		std::deque<int> ordered;
		ordered.push_back(start);
		return ordered;
	}

	// normal case
	auto n = end - start + 1;
	deque<int> ordered;
	long long mid = (n % 2 == 0) ? (n / 2) - 1 : (n / 2); // when converting to long long 2.5 becomes 2
	mid += start;
	minS[mid] = (n % 2 == 0) ? (n / 2) - 1 : (n / 2);
	maxS[mid] = n / 2;
	ordered.push_back(mid);

	// call for each remaining side
	auto left = order(start, mid - 1);
	auto right = order(mid + 1, end);

	// combine both sides
	while (!left.empty() || !right.empty()) {
		// specical case left is already empty
		if (left.empty()) {
			while (!right.empty()) {
				ordered.push_back(right.front());
				right.pop_front();
			}
			break;
		}

		// specical case right is already empty
		if (right.empty()) {
			while (!left.empty()) {
				ordered.push_back(left.front());
				left.pop_front();
			}
			break;
		}

		// both have element
		auto leftE = left.front();
		auto rightE = right.front();
		bool chooseLeft = true;
		// check which one to use
		if (minS[leftE] > minS[rightE]) chooseLeft = true;
		else if (minS[leftE] < minS[rightE]) chooseLeft = false;
		else if (maxS[leftE] >= maxS[rightE]) chooseLeft = true;
		else if (maxS[leftE] < maxS[rightE]) chooseLeft = false;

		if (chooseLeft) {
			ordered.push_back(leftE);
			left.pop_front();
		}
		else {
			ordered.push_back(rightE);
			right.pop_front();
		}
	}

	return ordered;
}

void main() {
	int t;
	long long n, k;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

	for (int i = 1; i <= t; ++i) {
		cin >> n >> k;  // read n

		// fill vectors
		occupiedBy = std::vector<int>(n);
		minS = std::vector<int>(n);
		maxS = std::vector<int>(n);

		auto ordered = order(0, n - 1);
		// indexOfLastPersonsStall 
		long long j = ordered[k-1];
		cout << "Case #" << i << ": " << maxS[j] << " " << minS[j] << endl;
	}
}
