#include <iostream>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <utility>
using namespace std;
string solve(string &s) {
	bool borrow = false;
	for (int i = s.length() - 2; i >= 0; i--) {
		char ci = s[i];
		char ci_1 = s[i + 1];
		
		if (ci_1 >= ci && !borrow) {
			
		}
		else {
			if (s[i] > '0') {
				borrow = false;
				s[i] = s[i] - 1;
				for (int k = i+1; k < s.length(); k++)
					s[k] = '9';
			}
			else {
				borrow = true;
			}
		}
	}
		
	
	s.erase(0, min(s.find_first_not_of('0'), s.size() - 1));
	return s;
}

int main() {

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cout << "Case #" << tc << ": ";
		string n;
		cin >> n;

		string rc = solve(n);
			cout << rc << '\n';
		
	}
}
