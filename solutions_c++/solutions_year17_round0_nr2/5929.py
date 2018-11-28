#include <iostream>
#include <string>

using namespace std;

int main()
{
	int total;
	cin>>total;
	for (int k = 0; k < total; ++k) {
		string s;
		cin>>s;
		int pos = s.size();
		for (int i = s.size()-1; i > 0; --i) {
			if (s[i] < s[i-1]) {
				if (s[i-1] != '0') s[i-1]--;
				pos = i;
			}
		}
		string res = "";
		string tmp(s.size()-pos, '9');
		if (s[0] != '0')	res += s.substr(0, pos);
		res += tmp;
		cout<<"Case #"<<k+1<<": "<<res<<endl; 
	}	

	return 0;
}