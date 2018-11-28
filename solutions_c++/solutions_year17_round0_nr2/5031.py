#include <iostream>
#include <vector>

using namespace std;

int main() {
	int t, T;
	cin >> t; T = t;
	while (t--) {
		string num; 
		cin >> num;
		int sz = num.size();

		int i = 0;
		while (i < sz - 1 && num[i+1] >= num[i])
			i++;

		// Already tidy
		if (i == sz - 1)
			goto done;

		// Set all to 9s and decrement current by 1
		num[i]--; 
		for (int j = i + 1; j < sz; ++j)
			num[j] = '9';

		// Go back, changing digits until the number becomes tidy again
		while (i > 0 && num[i-1] > num[i]) {
			num[i] = '9'; num[i-1]--;
			i--;
		}
		goto done;



		done:
			for (i = 0; (num[i] == '0') && (i < sz - 1); ++i);
			cout << "Case #" << T - t << ": " << num.substr(i) << "\n";
	}
	return 0;
}