#include <cstdlib>
#include <string>
#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int t_i = 0; t_i < t; t_i++) {

		string s;
		cin >> s;

		for (int j = s.length() - 1; j >= 1; j--) {
			char x = s[j];
			char y = s[j-1];
			int xk = x - '0';
			int yk = y - '0';
			if (yk > xk) {
				yk--;
				s[j-1] = '0' + yk;
				s[j] = '9';
				for (int i = j; i < s.length(); i++) {
					s[i] = '9';
				}
			}
		}
		int n = 0;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '0') {
				n++;
			}
		}
		s.erase(0, n);

		cout<<"Case #" <<t_i+1<<": "<<s<<endl;
		
	}

}