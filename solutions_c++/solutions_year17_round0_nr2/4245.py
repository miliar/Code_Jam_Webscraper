#include <iostream>
#include <string>
#include <stdio.h>
#include <sstream>

namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

using namespace std;

void output(int num, string text) {
	cout << "Case #" << num << ": " << text << endl;
}

void output(int num, int value) {
	cout << "Case #" << num << ": " << value << endl;
}

void output(int num, float value) {
	cout << "Case #" << num << ": " << value << endl;
}

string checkTidy(string s)
{
	string c;
	int n;
	if (s.length() == 1)
		return s;

	for(int i = 0, l = s.length()-1; i<l;i++)
	{
		if (s[i] > s[i+1])
		{
			c = s[i];
			sscanf(c.c_str(), "%d", &n);
			if (n == 1)
				return string(l, '9');
			else
			{
				s.replace(i, 1, patch::to_string(--n));
				s.replace(i+1, l - i, string(l - i, '9'));
				return checkTidy(s);
			}
		}
	}
	return s;
}

int main() {
  int t, n;
  string s;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> s;
    output(i, checkTidy(s));
  }
}

