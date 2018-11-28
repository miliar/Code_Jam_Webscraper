#include <cstdlib>
#include <string>
#include <iostream>
#include <math.h>
#include <vector>

using namespace std;


int check(string s) {
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == '-') {
			return i;
		}
	}
	return -1;
}

int main() {
	int t;
	cin >> t;
	for (int t_i = 0; t_i < t; t_i++) {
		string s;
		cin >> s;
		int k;
		cin >> k;

		int n = 0;

		int c = check(s);
		bool possible = true;

		while (c != -1) {
			if (c + k > s.length()) {
				possible = false;
				break;
			}
			for (int i = c; i < c + k; i++) {
				if (s[i] == '+') {
					s[i] = '-';
				} else {
					s[i] = '+';
				}
			}
			n++;
			c = check(s);
		}

		if (possible) {
			cout<<"Case #" <<t_i+1<<": "<<n<<endl;
		} else {
			cout<<"Case #" <<t_i+1<<": "<<"IMPOSSIBLE"<<endl;
		}
		
	}

}