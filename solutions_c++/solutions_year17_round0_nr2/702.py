#include<bits/stdc++.h>
using namespace std;
int main(){
	int T;
	cin >> T;

	for(int l = 1; l <= T; l++){
		string s;
		cin >> s;
		int ma[s.size()];
		int n = s.size();
		int i;
		for(i = 1; i < n; i++)
			if(s[i] < s[i-1])
				break;
		if(i == n){
			cout << "Case #" << l << ": " << s << endl;
			continue;
		}
		for(; i > 0; i--)
			if(s[i] > s[i-1])
				break;
		s[i]--;
		for(i++; i < n; i++)
			s[i] = '9';
		i = 0;
		if(s[0] == '0') i = 1;

		cout << "Case #" << l << ": ";
		for(; i < n; i++)
			cout << s[i];
		cout << endl;
	}

	return 0;
}