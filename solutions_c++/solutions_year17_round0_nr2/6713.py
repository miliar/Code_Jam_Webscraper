#include <bits/stdc++.h>
using namespace std;

inline string func(char last, string s) {
	//cout << last << " - " << s << endl;
	if(last > s[0]) return "-1";
	if(s.size() == 1) return s;

	string res = func(s[0], s.substr(1));
	if(res != "-1") return s.substr(0, 1) + res;

	res = s;
	res[0] = s[0] - 1;
	for(int i=1; i<(int) s.size(); ++i) res[i] = '9';
	if(last > res[0]) return "-1";
	else return res;
}

int main()
{
	int t, tc=0;
	cin >> t;

	while(t--) {
		string s;
		cin >> s;

		string res = func('0', s);
		int i;
		for(i=0; i<(int) res.size() && res[i] == '0'; ++i) ;
		cout << "Case #" << ++tc << ": " << res.substr(i) << "\n";
	}

	return 0;
}