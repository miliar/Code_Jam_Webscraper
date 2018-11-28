#include <bits/stdc++.h>
using namespace std;

bool checkTidy(auto& num) {
	int l=num.size();
	for (int i=1; i<l; i++)
		if((num[i-1] > num[i]))
			return false;

	return true;
}

void subtractBigNum (auto& num) {
	int carry = 0;
	int l = num.size()-1;
	for (int j=l; ; j--) {
		if (num[j] >= 1) {
			num[j]--;
			return;
		}
		else {
			num[j] = 9;
			carry=1;
		}
	}
}

int main() {
	int t;
	string n;
	cin >> t;
	for (int i=1; i<=t; i++) {
		cin >> n;
		vector<short> number;
		for (int i=0; i<n.length(); i++)
			number.push_back(n[i] - '0');

		while (1) {
			if (checkTidy(number)) {
				cout << "Case #" << i << ": ";
				int j=-1;
				while (number[++j] == 0);
				for (; j<number.size(); j++)
					cout << number[j];
				cout << '\n';
				break;
			}
			subtractBigNum(number);

		}
	}
	return 0;
}
