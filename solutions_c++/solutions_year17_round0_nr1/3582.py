#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int q = 1; q <= t; q++){
		string s;
		cin >> s;
		int k;
		int count = 0;
		cin >> k;
		cout << "Case #" << q << ": ";
		for(int i = 0; i <= s.length() - k; i++){
			if(s[i] == '-'){
				count++;
				for(int j = i; j < i+k; j++){
					if(s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		bool cek = true;
		for(int i = s.length() - k + 1; i < s.length(); i++){
			if(s[i] == '-'){
				cek = false;
				break;
			}
		}
		if(cek) cout << count << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}