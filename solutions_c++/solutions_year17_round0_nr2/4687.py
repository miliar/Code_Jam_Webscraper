#include <bits/stdc++.h> 
using namespace std;

string s;

void check() {
	int i, j;
	for (i = 1; i < s.length(); ++i)
	{
		if(s[i-1] <= s[i]);
		else {
			// cout<< "hhh";
			s[i-1] = char(int(s[i-1])-1);
			for(j = i; j<s.length(); j++)
				s[j] = '9';

			if(i-1 == 0 && s[i-1] == '0')
				s.erase(s.begin());
			// cout << s << endl;
			check();
		}
		/* code */
	}
}

int main(int argc, char const *argv[])
{
	int t;
	cin >> t;
	for (int u = 1; u <= t; ++u)
	{
		cin >> s;
		check();
		/* code */
		cout << "Case #" << u << ": " << s << "\n";
	}
	return 0;
}