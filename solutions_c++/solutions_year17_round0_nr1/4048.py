#include <bits/stdc++.h>
using namespace std;
int main(){
	long long int t;
	cin >> t; 
	for(long long int h=1;h<=t;h++){
		int k,fl=0,times=0;string s; cin >> s >> k;
		for(int i=0;i<=s.length()-k;i++){
			if(s[i] == '-'){
				for(int j=i;j<i+k;j++){
					if(s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
				times++;
			}
		}
		for(int i=0;i<s.length();i++){
			if(s[i] == '-') fl = 1;
		}
		cout << "Case #" << h << ": "; 
		if(fl == 1) cout << "Impossible";
		else{
			cout << times;
		}
		cout << endl;
	}
	return 0;
}