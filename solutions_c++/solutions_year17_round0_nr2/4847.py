#include <iostream>
#include <string>

using namespace std;

long long f() {
	long long n; cin >> n;
	string s = to_string(n);
	for (int i = s.size() - 1; i > 0; --i)
		if (s[i] < s[i-1]) {
			for (int j = i; j < s.size(); ++j)
				s[j] = '9';
			--s[i-1];
		}
	return stoll(s);
}

int main() {
	int t; cin >> t;
	for (int x = 0; x < t; ++x)
		cout << "Case #" << x+1 << ": " << f() << endl;
}
