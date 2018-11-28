#include <iostream>
#include <string>
using namespace std;
int main (void) {
	int t; cin >> t;
	for (int y = 1; y <= t; y++) {
		string s; cin >> s;
		int flag= 0;
		//check first if its tidy
		int c = 0;
		for (int i =0; i < (int)s.size()-1; i++ ) {
			if (s[i] <= s[i+1])
				c++;
		}
		for (int i = 0; i < (int)s.size(); i++) {
			if (c == (int)s.size() - 1)
				break;
			if (i == (int)s.size()-1 && flag != 1) {	//last element
				//decrease by one 
				s[i]--;
			}
			else if (i == (int)s.size()-1 && flag == 1) {
				//cout << " ** " << i << " ** "<< endl;
				break; 
			}
			else {
				if (s[i] > s[i+1]) { //decrease s[i] and maximize the rest
					s[i]--;
					for (int j = i+1; j < (int)s.size(); j++)
						s[j] = '9';
					flag = 1;
					i = -1;
				}
			}
		}
		int leading0 = 0;
		for (int i = 0; i < (int)s.size(); i++) {
			if (leading0 == 0) {
				if (s[i] != '0') {
					cout << "Case #" << y << ": " << s[i];
					leading0 = 1;
				}
				else
					continue;
			}
			else
				cout << s[i];
		}
		cout << endl;
	}

	return 0;
}