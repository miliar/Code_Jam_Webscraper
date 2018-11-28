#include <iostream>
#include <string>
using std::cin;
using std::cout;

inline bool is_down(std::string& s, int i) {
	return s[i] == '-';
}

inline void flip(std::string& s, int i) {
	if (s[i] == '+')
		s[i] = '-';
	else
		s[i] = '+';
}

void flip_range(std::string& s, int from, int length) {
	if (from+length > s.length())
		return;

	for (int i = from; i < from+length; i++)
		flip(s,i);
}

bool is_fixed(std::string& s) {
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == '-')
			return false;
	}
	return true;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		std::string s;
		int K;
		cin >> s >> K;
		int noper = 0;
		for (int i = 0; i < s.length(); i++) {
			if (is_down(s,i)) {
				noper++;
				flip_range(s,i,K);
			}
		}
		cout << "Case #" << t << ": " ;
		if (is_fixed(s))
			cout << noper << "\n";
		else
			 cout << "IMPOSSIBLE\n";
	}
	return 0;
}
