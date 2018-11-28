#include<iostream>
using namespace std;
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t, tt, i;
	string s;
	cin >> t;
	for(tt=1; tt<=t; ++tt)
	{
		cin >> s;
		start:
		for(i=0; i<s.length()-1; ++i)
		{
			if(s[i+1] < s[i])
				break;
		}
		if(i<s.length()-1)
		{
			s[i] = s[i] - 1;
			for(++i; i<s.length(); ++i)
				s[i] = '9';
			goto start;
		}
		cout << "Case #" << tt << ": ";
		for(i=0; i<s.length() && s[i]=='0'; ++i);
		for(; i<s.length(); ++i)
			cout << s[i];
		cout << endl;
	}
 	return 0;
}

