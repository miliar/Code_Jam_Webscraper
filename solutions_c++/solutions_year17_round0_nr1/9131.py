#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <string>
#include <cstdio>
using namespace std;
int main() {

	freopen ("A-large.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	
	int t;
	cin >> t;

	for (int test = 1; test <= t; test++) {
		string s;
		cin >> s;
		int k;
		cin >> k;

		int flips = 0;
		bool is_complete = false;
		bool is_posible = false;

		while (!is_complete) {
			int minus_cnt = 0;
			int first_minus_index = -1;
			for (int i = 0; i < s.size(); ++i) {
				if (s[i] == '-') {
					first_minus_index = i;
					minus_cnt++;
					break;
				}
			}
			for (int i = first_minus_index + 1; i < s.size(); i++) {
				if (s[i] == '-') {
					minus_cnt++;
				}
			}	
			if (minus_cnt > 1) {
				is_complete = false;
			} else if (minus_cnt == 1) {
				is_posible = false;
			} else {
				is_posible = true;
				is_complete = true;
			}

			if (!is_complete) {
				int start = first_minus_index;
				int range = start + k;
				// cout << start << " " << range << " " << s.size() << endl;
				if (range <= s.size() && start != -1) {
					for (int i = start; i < range; i++) {
						if (s[i] == '+') {
							s[i] = '-';
						} else {
							s[i] = '+';
						}
					}
					flips++;
					// cout << s << endl << endl;
				} else {
					is_posible = false;
					is_complete = true;
				}
			}
			
		}

		if (is_posible) {
			cout << "Case #" << test << ": " << flips << endl;
		} else {
			cout << "Case #" << test << ": IMPOSSIBLE" << endl;
		}

	}
	return 0;
}