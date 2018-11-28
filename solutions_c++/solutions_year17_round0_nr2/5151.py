#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int next() {int x; cin >> x; return x;}

int main() {

	int tests = next();
	for (int test = 1; test <= tests; test++) {
		string s;
		cin >> s;
		
		string answ = "";
		bool fall = false;
		for (int i = 0; i < s.size(); i++) {
			if (fall) answ += "9";
			else {
				bool small = true;
				for (int j = i + 1; j < s.size(); j++) {
					if (s[j] > s[i]) break;
					if (s[j] < s[i]) small = false;
				}

				if (small) answ += s[i];
				else {
					answ += (char)(s[i] - 1);
					fall = true;
				}
			}

		}
		while (answ[0] == '0') answ = answ.substr(1);
		
		cout << "Case #" << test << ": " << answ << "\n";
		//printf("Case #%d: %s\n", test, s);

	}
}