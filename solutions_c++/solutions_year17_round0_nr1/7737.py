#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int f = 0;

bool analizarString (string s, int k) {
	for (int i = 0; i < s.length() - (k - 1); i++) {
		if (s.at(i) == '-') {
			for (int j = i; j < i + k; j++) {
				if (s.at(j) == '+') {
					s.at(j) = '-';
				} else if (s.at(j) == '-') {
					s.at(j) = '+';
				}
			}
		f++;
		}
	}
	int n=s.length()-k;
	while(n<s.length()){
		if(s[n]=='-') return false;
		n++;
	}
	return true;
}

int main(int argc, char *argv[]) {
	int t, k;
	string s;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> s;
		cin >> k;
		cout << "Case #" << i + 1 << ": ";
		if (analizarString(s, k)) {
			cout << f << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
		f = 0;
		s = "";
	}
	
	return 0;
}

