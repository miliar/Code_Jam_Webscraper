#include <bits/stdc++.h>

using namespace std;


/*
algorithm:
if we are strictly less than n, fill with 9's and return
otherwise, if this digit is less than the last one we placed, pop two, replace with second-1, fill with 9s and return
*/

vector<int> first_lucky(long long n) {
	vector<int>digits;
	while (n) {
		digits.push_back(n%(10LL));
		n /= 10LL;
	}
	reverse(digits.begin(),digits.end());
	vector< int > acc;
	acc.push_back(digits[0]);
	for (int i = 1; i < digits.size(); i++) {
		if (digits[i] < acc.back()) {
			int k = acc.back();
			acc.pop_back();
			while (acc.back() == k) {
				acc.pop_back();
				i--;
			}
			acc.push_back(k-1);
			while (i < digits.size()) {
				acc.push_back(9);
				i++;
			}
		} else {
			acc.push_back(digits[i]);
		}
	}
	return acc;
}

int main() {
	int T, C = 1;
	cin >> T;
	while (T--) {
		long long n;
		cin >> n;
		cout << "Case #" << C++ << ": ";
		auto k = first_lucky(n);
		int i = 0;
		while (k[i]==0)
			i++;
		while(i<k.size())
			cout << k[i++];
		cout << endl;
	}
}