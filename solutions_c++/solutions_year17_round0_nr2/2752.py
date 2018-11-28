#include <bits/stdc++.h>

using namespace std;

void solve(int id) {
	string ex;
	cin >> ex;

	string my = ex;
	for (char& c : my) {
		c = '1';
	}

	if (my > ex) {
		my.pop_back();
		for (char& c : my) {
			c = '9';
		}
	} else {
		for (size_t i = 0; i < my.size(); ++i) {
			for (char c = my[i] + 1; c <= '9'; ++c) {
				for (size_t j = i; j < my.size(); ++j) {
					my[j] = c;
				}
				if (my > ex) {
					for (size_t j = i; j < my.size(); ++j) {
						my[j] = c - 1;
					}
					break;
				}
			}
		}
	}
		
	printf("Case #%d: %s\n", id, my.c_str());
}

int main() {
	int t;
	cin >> t;

	int id = 1;
	while (t --> 0) {
		solve(id++);
	}

	return 0;
}
