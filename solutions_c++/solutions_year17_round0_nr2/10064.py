#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	string s;

	cin >> t;

	for (int x = 1; x<=t; ++x) {
		cin >> s;
		cout << "Case #" << x << ": ";
		if(s == "0") {
			cout << s << endl;
			continue;
		}
		for (int i = s.length()-1; i > 0; --i)
		{
			if (s[i] < s[i-1])
			{
				--s[i-1];
				s[i] = '9';
			}
		}
		int i;
		for (i = 0; i < s.length()-1; ++i)
		{
			if (s[i] > s[i+1])
			{
				break;
			}
		}
		for (++i; i < s.length(); ++i)
		{
			s[i] = '9';
		}
		
		string::iterator it = s.begin();
		while(it != s.end() && *it<='0') ++it;
		while(it != s.end()) {
			cout << *(it++);
		}
		cout << endl;
	}

	return 0;
}