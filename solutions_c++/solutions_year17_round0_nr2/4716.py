#include <iostream>

using namespace std;

int main() {
	int numCases;
	cin >> numCases;
	string num;
	int cnt = 0;
	while (cin >> num) {
		int length = num.length();
		int k = length;
		for (int i=num.length()-1; i>0; --i) {
			if (num[i-1] > num[i]) {
				for (int j=i; j<k; ++j)
					num[j] = '9';
				k = i;
				num[i-1]--;
			}
		}
		while (!num.empty() && num[0] == '0') num = num.substr(1);
		if (num.empty()) num = "0";
		cout << "Case #" << ++cnt << ": " << num << endl;
	}
	return 0;
}