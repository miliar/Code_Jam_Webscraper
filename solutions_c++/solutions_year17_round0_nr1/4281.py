#include <iostream>
#include <string>
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

int c = 0;

string rotate(string s) {
	string r;

	for(int i = 0, l = s.length(); i<l; i++)
	{
		r += s[i] == '-' ? '+' : '-';
	}
	c++;
	return r;
}

int calc(string s, int m)
{
	int f;
	string p;
	//cout << c;
	if ((f = s.find('-')) == string::npos)
		return c;

	if (f+m <= s.length()) {
		s.replace(f,m,rotate(s.substr(f, m)));	
		//cout << s << endl;
		return calc(s,m);
	}
	
	return -1;
}

int main() {
  int t, n, m;
  string s, imp = "IMPOSSIBLE";

  cin >> t;
  for (int i = 1; i <= t; ++i) {
  	c = 0;
    cin >> s >> m;
    n = calc(s, m);
    if (n < 0)
    	output(i, imp);
    else
    	output(i, n);
  }
}

