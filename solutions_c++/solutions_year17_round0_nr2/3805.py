#include <bits/stdc++.h>

using namespace std;

int main(){
	int k;
	cin >> k;
	ofstream out("ofile2");

	for(int p=1;p<=k;p++){
		string s;
		cin >> s;

		for(int i=s.length()-2;i>=0;i--){
			if(s[i]>s[i+1]){
				s[i]--;
				for(int j=i+1;j<s.length();j++){
					s[j]='9';
				}
			}
			//cout << 
		}
		cout << s << endl;
		if(s[0]=='0'){
			s = s.substr(1,s.length()-1);
		}
		cout << s << endl;
		out << "Case #" << p << ": " << s << endl;
	}
}