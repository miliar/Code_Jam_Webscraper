#include <iostream>
#include <string>

using namespace std;

int t,k,count = 0;
string s;

int main(){
	cin >> t;
	for(int i = 1; i <= t; i++){
		cin >> s >> k;
		int l = s.length();
		for(int j = 0; j <= l-k; j++){
			if(s[j] == '-'){
				for(int u = 0; u < k; u++){
					if(s[j+u] == '-') s[j+u] = '+';
					else s[j+u] = '-';
				}
			count++;
			}
		}
		int check = 0;
		for(int j = 0; j < l; j++){
			if(s[j] == '-') check = 1;
		}
		cout << "Case #" << i << ": ";
		if(check == 1) cout << "IMPOSSIBLE";
		else cout << count;
		cout << endl;
		count = 0;
	}
	return 0;
}
