/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;


/*
 * The Algorithm:
 * 	find the largest non decreasing prefix in the number, we'll call this prefix "nice_prefix" --done--
 * 	if reached the end of the number => the number itself is the answer (end and go to next data set) --done--
 * 	if the last digit of "nice_prefix" is '1' => print the digit '9' repeated size(number) - 1 (end and go to next data set) --done--
 * 	in the "nice_prefix" get the largest suffix consisting of the same digit "nice_suffix" --done--
 * 	change the first digit in "nice_suffix" to itself - 1 --done--
 * 	change all the next digits in number to '9' --done--
 * 	print number (end and go to next data set) --done--
 */

void print_ans(int &K, string ans) {
	cout << "Case #" << K++ << ": " << ans << endl;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, K = 1;
	cin >> T;
	while (T--) {
		string s;
		int n, i, j;

		cin >> s;
		n = s.size();

		for (i = 0; i < n - 1; ++i) {
			if (s[i] > s[i + 1]) break;
		}

		if (i == n - 1) {
			print_ans(K, s);
			goto NXT;
		}

		if (s[i] == '1') {
			print_ans(K, string(n - 1, '9'));
			goto NXT;
		}

		for (j = i; j >= 0; --j) {
			if (j == 0 || s[j - 1] != s[j]) break;
		}

		s[j]--;
		for (i = j + 1; i < n; ++i) s[i] = '9';

		print_ans(K, s);

		NXT:;
	}
	return 0;
}
