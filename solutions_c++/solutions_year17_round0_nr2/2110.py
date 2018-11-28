#include <iostream>
#include <string>
using namespace std;
int main() {
	int T; cin >> T;
	
	string s;
	for(int t = 0; t < T; t++) {
		cin >> s;

		
		for(int i = 1; i < s.length(); i++) {
			if (s[i]<s[i-1]) {

				for(int j = i; j < s.length(); j++) s[j] = '9';

				i = i - 1;
				while (i > 0 && s[i]==s[i-1]) 
				{
					s[i] = '9';
					i--;
				}

				s[i] -= 1;
					
				break;	
			}
		}
		cout << "Case #" << t+1 << ": ";
		
		int idx=0;
		while (s[idx]=='0'){idx++;}
		for(;idx < s.length();idx++) {
			cout << s[idx];
		}
		cout << endl;
		

	}
	return 0;
}