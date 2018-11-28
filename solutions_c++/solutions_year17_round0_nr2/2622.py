#include<string>
#include<iostream>

using namespace std;


int main() {

	int t; cin >> t;
	for(int i = 0; i < t; i++){
		string s; cin >> s;
		// first ulta
		int j;
		for(j = 0; j+1 < s.size(); j++) {
			if(s[j] > s[j+1]) {
				int k = j;
				for(; k >= 0; k--){
					if(k > 0 && s[k-1] == s[j]){
						continue;
					}else break;
				} 
				
				for(int p = k+1; p < s.size(); p++) s[p] = '9';
				s[k] = (char)( s[k] - 1);
				break;
			}
		}
		
		cout << "Case #" << i+1 << ": ";
		if(s[0] == '0') {
			j = 1;
		}else j = 0; 
		for(; j < s.size(); j++) cout << s[j];
		cout << endl;
	}
	return 0;
} 	
