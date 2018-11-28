#include <iostream>
using namespace std;

int main(){
	int t; cin >> t;
	for (int i=0;i<t;i++){
		string s; cin >> s;
		for (int j=s.length()-1;j>=1;j--){
			if (s[j] < s[j-1]){
				s[j-1]--;
				for (int k=j;k<s.length();k++) s[k] = '9';
			}
		}
		cout << "Case #" << i+1 << ": ";
		if (s[0] == '0'){
			for (int j=1;j<s.length();j++) cout << s[j];
		} else cout << s;
		cout << '\n';
	}
}
