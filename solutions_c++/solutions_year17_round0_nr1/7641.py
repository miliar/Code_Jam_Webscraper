#include <iostream>
#include <string>

using namespace std;

int main (void) {
	int T ; cin >> T;
	
	for (int t = 1; t <= T; t++) {
		int count = 0, flag = 0;
		string s; 
		int k; cin >> s >> k;
		
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '-' && i <= (int)s.size()-k) {
				count++;
				for (int j = i; j < k+i; j++){
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		}
				
		for (int j = 0; j < s.size(); j++){
			if (s[j] == '-') {
				flag = 1;
				break;
			}
		}		
		
		cout << "Case #" << t << ": ";
		if(flag == 0)
			cout << count << endl;
		else
			cout << "IMPOSSIBLE"<<endl;	
	}
	
	return 0;
}