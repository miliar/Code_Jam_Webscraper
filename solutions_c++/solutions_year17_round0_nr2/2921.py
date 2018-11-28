#include <iostream>
#include <string>

using namespace std;

string get_last_tidy(const string& n) {
	int start_plain, end_rise;
	char prev = '0';
	for (int i = 0; i < n.length() && n[i] >= prev; ++i) {
		end_rise = i;
		prev = n[i];
	}

	if (end_rise == n.length() - 1) {
		return n;
	}

	start_plain = end_rise;
	while (start_plain > 0 && n[start_plain - 1] == n[end_rise]) {
		--start_plain;
	}

	string res;
	for (int i = 0; i < start_plain; ++i) {
		res.push_back(n[i]);
	}

	if (n[start_plain] != '1') {
		res.push_back(n[start_plain] - 1);
		
	}
	for (int i = 0; i < n.length() - start_plain - 1; ++i) {
		res.push_back('9');
	}
	return res;
}

int main() {
	int t;
	string n;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cin >> n;
		cout << "Case #" << i + 1 << ": " << get_last_tidy(n) << endl;
	}
	return 0;
}