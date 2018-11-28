#include <bits/stdc++.h>
/*
TASK: hidden
LANG: C++11
*/
using namespace std;
typedef long long ll;
typedef pair<int, int> pair2;
typedef pair<int, pair<int, int> > pair3;
typedef pair<int, pair<int, pair<int, int> > > pair4;
#define MAXN 10000
//#define INFINITY 1000000000000000L
#define mp make_pair
#define add push_back
#define remove pop

int n;
int operations;
ll solve(int * digits, int current, int lowerBound, bool isAtLimit) {
	if (!isAtLimit) {
		ll answer = 0;
		for (int i = 0; i < n - current; i++) {
			answer *= 10;
			answer += 9;
		}
		return answer;
	}

	if (lowerBound > digits[current]) {
		return -1;
	}

	if (current == n - 1) {
		return digits[current];
	}

	//isAtLimit tells us if the first digits have been at the maximum they possibly could, restricting our current choice of digits.

	int start = lowerBound;
	int end = digits[current];

	while (start <= end) {
		int mid = (start + end) / 2;

		ll answer = solve(digits, current + 1, mid, (mid == digits[current]) && isAtLimit);

		if (answer != -1) {
			start = mid + 1;
		} else {
			end = mid - 1;
		}
	}

	if (end < lowerBound) {
		return -1;
	}

	//operations++;
	//cout << end << '\n';
	ll ret = end;
	for (int i = 0; i < n - current - 1; i++) {
		ret *= 10;
	}

	ret += solve(digits, current + 1, end, (end == digits[current]) && isAtLimit);
	return ret;
}

int main() {
	//freopen("friendcross.in", "r", stdin);
	//freopen("friendcross.out", "w", stdout);
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL);

	int T;
	cin >> T;
	int counter = 1;

	while (T--) {
		ll number;
		cin >> number;

		//Recursive search. For example if the int range we have right now is 0..9 and it turns out it's possible with 5, then we only have to bsearch on 6...9.

		ll temp = number;

		n = 0;
		while (temp > 0) {
			temp /= 10;
			n++;
		}

		int * digits = new int[n];

		for (int i = n - 1; i >= 0; i--) {
			digits[i] = number % 10;
			number /= 10;
		}

		cout << "Case #" << counter++ << ": " << solve(digits, 0, 0, true) << '\n';
	}
}