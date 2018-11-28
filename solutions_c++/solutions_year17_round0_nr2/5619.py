#include <iostream>
#include <string>
using namespace std;
typedef unsigned long long ull;

bool checkTidy(ull n) {
	string s = to_string(n);
	for (int i = 1; i < s.length(); ++i) {
		if (s[i-1] <= s[i]) continue;
		return false;
	}
	return true;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		ull n;
		string res;
		cin >> n;
		while (!checkTidy(n)) {
			res.insert(0, "9");
			n /= 10;
			n -= 1;
		}
		if (n > 0) res.insert(0, to_string(n));
		
		
		cout << "Case #" << i << ": " << res << endl;
	}
	
	return 0;
}