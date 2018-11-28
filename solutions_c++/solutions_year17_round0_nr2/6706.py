#include <iostream>
#include <string>

using namespace std;

int main() {
	int test_cases;
	cin >> test_cases;
	for (int tc = 1; tc <= test_cases; tc++) {
		long long n;
		cin >> n;
		string num = to_string(n);
		do {
			int i = 1;
			int sz = (int)num.size();
			for ( ; i < sz; i++) {
				if (num[i] < num[i-1]) { // violation of non decreasing property
					num[i] = '9';
					num[i-1] -= 1;
					for (int j = i+1 ; j < sz; j++) {
						num[j] = '9'; // borrow means everyone to the right becomes a 9
					}
					n = stoll(num);
					num = to_string(n);
					break;
				}
			}
			if (i == sz) // if we made it to the end
				break;
		} while (1);

		cout << "Case #" << tc << ": " << n << endl;
	}
}