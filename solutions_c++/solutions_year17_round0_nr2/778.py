#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;

string solve(string s){
	int n = s.length();
	if (n <= 1) return s; 
	int i=n-1;
	while(i>0 && s[i] >= s[i-1]){--i;}
	if(i==0) return s;

	
	--s[i-1];
	for(int j=i;j<n;++j){s[j] = '9';}
	return solve(s.substr(0,i))+s.substr(i);
}

int main(){
	int T;
	string s;
	cin >> T;
	for(int t=1;t<=T;++t) {
		cin >> s;
		cout << "Case #" << t << ": ";
		string res = solve(s);
		int i = 0;
		while(i<res.length() && res[i] == '0') ++i; 
		cout << res.substr(i) << endl;
	}
}