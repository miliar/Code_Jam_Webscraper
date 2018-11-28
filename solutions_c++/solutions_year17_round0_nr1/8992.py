#include <iostream>  
#include <vector>
#include <string>

using namespace std; 
int main() {
	int t;
	string s;
	int f;
	
	int r = 0;
	int i = 0;
	
	cin >> t;  
	for (int k = 1; k <= t; ++k) {
		r = 0;
		i = 0;
		cin >> s;
		cin >> f;
		cerr << s << " " << f << endl;
		cerr << "len " << s.length() << endl;
		while (i < s.length()) {
			for (; i<s.length(); i++)
				if (s[i] == '-')
					break;
			cerr << "i " << i << endl;
			if (i == s.length())
				break;
			if (i+f > s.length()) {
				r = -1;
				break;
			}
			cerr << i << endl;
			for (int j=0; j<f; j++)
				if (s[i+j] == '+')
					s[i+j] = '-';
				else
					s[i+j] = '+';
			r++;
			cerr << s << " " << f << endl;
		}
		if (r == -1)
			cout << "Case #" << k << ": " <<  "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << k << ": " << r << endl;
		
		//		exit(0);
	}
	return 0;
}
