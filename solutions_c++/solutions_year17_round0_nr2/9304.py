#include <iostream>  
#include <vector>
#include <string>

using namespace std; 
int main() {
	int t;
	string s;
	string r;
	int i;
	cin >> t;  
	for (int k = 1; k <= t; ++k) {
		r = "";
		
		cin >> s;
		cerr << s << endl;
		i = s.length() - 1;
		while (i > 0) {
			if (s[i] < s[i-1] || s[i] == '0') {
				for (int p=i; p<s.length(); p++)
					s[p] = '9';
				if (s[i-1] > '0')
					s[i-1] = s[i-1] - 1;
				else
					s[i-1] = '9';
			}
			cerr << s << endl;
			i--;
		}
		cout << "Case #" << k << ": " << stol(s) << endl;
	}

	return 0;
}
