#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int i=0;i<t;i++){
		string s;
		cin >> s;
		if(s.length() == 1){
			cout << "Case #" << (i+1) << ": " << s << endl;
			continue;
		}
		for(int j=s.length()-1;j>0;j--){
			if(s[j] < s[j-1]){
				s[j-1] = s[j-1] == '0' ? '9' : (s[j-1] - 1);
				for(int k=j;k<s.length();k++){
					s[k] = '9';
				}
				j = s.length();
			}
		}
		int index = 0;
		for(int j=0;j<s.length();j++){
			if(s[j] == '0'){
				index++;
			}
			else{
				break;
			}
		}
		if(index == 0) cout << "Case #" << (i+1) << ": " << s << endl;
		else if(index == s.length()) cout << "Case #" << (i+1) << ": " << "0" << endl;
		else cout << "Case #" << (i+1) << ": " << s.substr(index,s.length()) << endl;
	}
}