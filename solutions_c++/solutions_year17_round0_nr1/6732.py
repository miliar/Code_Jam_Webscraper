#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int test_cases;
	cin >> test_cases;
	for (int tc = 1; tc <= test_cases; tc++) {
		string s;
		cin >> s;
		int k; 
		cin >> k;
		int n = (int)s.size();
		vector<int> values(k + n + k, 0);

		int accumulator = 0;
		int num_ops = 0;
		bool impossible = false;
		int i = 0, j = k; // i indexes + and - string, j indexes array where we store whether to flip at that leftmost position
		for ( ; i <= n - k; i++, j++) { // phase 1: just accumulate results and determine flips
			if (s[i] == '+' && accumulator == 1 || s[i] == '-' && accumulator == 0) { // in this case: 1
				num_ops++;
				accumulator ^= 1;
				values[j] = 1;
			}
			accumulator ^= values[j-k+1];
		}
		for ( ; i < n; i++, j++) { // phase 2: we've determined all of the flips, but consistency must still be checked where there is redundancy
			if (s[i] == '+' && accumulator == 1 || s[i] == '-' && accumulator == 0) {
				impossible = true; // inconsistency found
				break;
			}
			//accumulator ^= (s[i] == '+' ? 0 : 1);
			accumulator ^= values[j-k+1];
		}
		if (impossible) {
			cout << "Case #" << tc << ": " << "IMPOSSIBLE" << endl;
		} else { 
			cout << "Case #" << tc << ": " << num_ops << endl;
		}
	}
}