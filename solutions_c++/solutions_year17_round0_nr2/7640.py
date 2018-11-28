#include <iostream>
#include <string>

using namespace std;

int main (void) {
	int T ; cin >> T;
	
	for (int t = 1; t <= T; t++) {
		string s; cin >> s;
		for (int i = 0; i < (int) s.size()-1; i++) {
			if (s[i+1] < s[i]){
				s[i]--;
				for (int j = i+1; j < s.size(); j++){
					s[j]='9';
				}
				i = -1;	
			}
		}
		bool a = false;
		cout << "Case #"<<t<<": ";
		for (int i = 0; i< s.size(); i++){
			if (s[i] != '0' || a == true) {
				a = true;
				cout << s[i];
			}	
		}
		cout<< endl;
	}
	
	return 0;
}