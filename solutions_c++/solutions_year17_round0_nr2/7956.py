#include <iostream>

using namespace std;


int main() {
	int T;
	 
	cin >> T;
	
	for(int i = 1; i <=T; i++) {
		string s;
		cin >> s;

		string ans = "";

		int len;
		len = s.length();

		int index = -1;

		int isSpecial = false;

		for(int j = 1; j < len; j++) { 		
                	if(s[j] < s[j-1]) {
				if(s[j-1] == '1' && s[j] == '0') isSpecial = true;
				index = j-1;
				break;
			}

		}


		if(isSpecial) {
			for(int j = 0; j < len-1; j++) {
				ans += '9';
			}
			cout << "Case #" << i << ": " << ans << endl;

		}
		else if(index == -1) {
			cout << "Case #" << i << ": " << s << endl;
		}
		else {
			for(int j = index; j >= 1; j--) {
				if(s[j] == s[j-1]) {
					index = j-1;
					continue;
				}
				else {

					break;
				}

			}


			s[index] = s[index] - '1' + '0';

			for(int j = index+1; j < len; j++) {
                         	s[j] = '9';

			}

			cout << "Case #" << i << ": " << s << endl;
		}

	}


}
