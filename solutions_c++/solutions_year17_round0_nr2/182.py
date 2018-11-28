#include <iostream>
#include <string>

int main() {
	int t;
    std::cin >> t;
	std::string s;
    for (int testCase = 1; testCase <= t; testCase++) {
		std::cin >> s;
		int len = s.size();
		int conflict = 0;
		for (int i = 1; i < len; i++) {
			if (s[i] < s[i - 1]) {
				conflict = i;
				break;
			}
		}
		if (conflict) {
			for (int i = conflict; i < len; i++) {
				s[i] = '9';
			}
			do {
				s[conflict] = '9';
				conflict--;
				s[conflict]--;
			} while (conflict && s[conflict] < s[conflict - 1]);
		}
		if (s.front() == '0' && len > 1)
			s = s.substr(1);
		std::cout << "Case #" << testCase << ": ";
		std::cout << s << std::endl;
    }
    return 0;
}
