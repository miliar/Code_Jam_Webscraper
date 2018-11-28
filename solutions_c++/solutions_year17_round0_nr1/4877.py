#include <iostream>

using namespace std;

int main() {
	int z;
	cin >> z;
	
	for(int zz = 1; zz <= z; zz++) {
		string text;
		int s;
		cin >> text >> s;
		int n = text.length();
		text = " " + text;
		
		int minimum = 0;
		
		for(int i = 1; i <= n - s + 1; i++) {
			if(text[i] == '+') {
				continue;
			}
			minimum++;
			
			for(int p = 1; p <= s; p++) {
				if(text[i + p - 1] == '-') {
					text[i + p - 1] = '+';
				} else {
					text[i + p - 1] = '-';
				} 
			}
		}
		
		bool OK = true;
		
		for(int i = n - s + 2; i <= n; i++) {
			if(text[i] == '-') {
				OK = false; break;
			}
		}
		
		cout << "Case #" << zz << ": "; 
		
		if(OK == true) {
			cout << minimum << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
			
	}
	return 0;
}
