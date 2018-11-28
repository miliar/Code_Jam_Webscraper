#include <iostream>
#include <string>
using namespace std;

int main() {
	int t,k;
	string s;
	cin >> t;
	for(int a = 0;a < t;a++){
		int res = 0;
		cin >> s >> k;
		for(int i = 0;i < s.length() - k + 1;i++){
			if(s[i] == '-'){
				res++;
				for(int j = 0;j < k;j++) {
					if(s[i + j] == '+') s[i + j] = '-';
					else s[i + j] = '+';
				}
			}
		}
		bool flag = true;
		for(int i = 0;i < s.length();i++) if(s[i] == '-') flag = false;
		if(flag) cout << "Case #" + to_string(a + 1) + ": " + to_string(res) << endl;
		else cout << "Case #" + to_string(a + 1) + ": IMPOSSIBLE"<< endl;
	}
	return 0;
}