#include <bits/stdc++.h>

using namespace std;

int solve(int idx, string &s, bool flag){
	if(flag) s[idx]--;

	if(idx==0){
		if(s[idx]<='0'){
			s.pop_back();
			return 0;
		}

		return (int)s.size();
	}

	if(s[idx]<s[idx-1] || s[idx]<'0')
		return min(idx, solve(idx-1, s, true));

	return solve(idx-1, s, false);
}

int main(){
	int t;

	cin >> t;

	for(int y=1; y<=t; y++){
		string s;

		cin >> s;

		int aux=solve(s.size()-1, s, false);
		for(int i=aux; i<(int)s.size(); i++)
			s[i]='9';

		printf("Case #%d: %s\n", y, s.c_str());
	}

	return 0;
}
