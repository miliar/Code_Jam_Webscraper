#include <bits/stdc++.h>

using namespace std;

void int_to_array(vector<int> &ip_array, long long input) {
	while (input != 0) {
		int rem = (int) (input % 10);
		ip_array.push_back(rem);
		input /= 10;
	}
}

int main() {
	int t;
	cin >> t;
	for (int q = 1; q <= t; q++) {
		long long input;
		bool flag = true;
		cin >> input;
		vector<int> ip_array;
		int_to_array(ip_array, input);
		for (int i = 1; i < ip_array.size(); i++) {
			if (ip_array[i] > ip_array[i - 1]) {
				ip_array[i] -= 1;
				for (int j = i - 1; j >= 0; j--) {
					ip_array[j] = 9;
				}
			}
		}
		int idx = ip_array[ip_array.size() - 1] == 0 ? ip_array.size() - 2 : ip_array.size() - 1;
		cout << "Case #" << q << ": ";
		while (idx >= 0) {
			cout << ip_array[idx--];
		}
		cout << endl;
	}
	return 0;
}
