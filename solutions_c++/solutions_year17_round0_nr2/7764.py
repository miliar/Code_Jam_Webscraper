#include <iostream>
using namespace std;

int main(void){
	int t; cin >> t;
	for(int tt = 1; tt <= t; tt++){
		string s;
		cin >> s;
		for(int i = 0; i < s.size() - 1; i++){
			if(s[i] > s[i+1]){
				for(int j = i + 1; j < s.size(); j++){
					s[j] = '9';
				}
				int k = s[i];
				s[i]--;
				for(int j = i - 1; j >= 0; j--){
					if(s[j] != k) break;
					s[i] = '9';
					s[j] = s[j] - 1;
				}
				break;
			}
		}
		cout << "Case #" << tt << ": ";
		if(s[0] != '0') cout << s[0];
		for(int i = 1; i < s.size(); i++) cout << (s[i] == '0' ? '9' : s[i]);		
		cout << endl;	
	}
	return 0;
}
