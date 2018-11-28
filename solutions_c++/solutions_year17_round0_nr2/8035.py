#include <fstream>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int findDeclineIndex(char* s, int length)
{
	int i;
	for(i = 1; i < length; i++)
	{
		if(s[i] < s[i - 1])
			return i - 1;
	}
	return -1;
}

string solve(string str)
{
	char* s = new char [str.length()+1];
	std::strcpy (s, str.c_str());
	int k = findDeclineIndex(s, str.length());
	if(k == -1) return s;
	int i;
	for(i = k + 1; i < str.length(); i++)
	{
		s[i] = '9';
	}
	for(i = k; i >0; i--)
	{
		if(s[i] == s[i - 1])
		{
			s[i] = '9';
		}
		else
		{
			s[i]--;
			return s;
		}
	}
	s[i]--;
	if(s[i] == '0')
		return s + 1;
	return s;
}

int main()
{
	int T;
	ifstream cin("B-large.in", ifstream::in);
	ofstream cout("B-large.out", ofstream::out);
	cin >> T;
	string s;
	int i;
	for(i = 1; i <= T; i++)
	{
		cin >> s;
		cout << "Case #" << i << ": " << solve(s) << endl;
	}
}