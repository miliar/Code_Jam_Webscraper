/*
Google Code Jam 2017
Qualification Round
B: Tidy Numbers
*/

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

bool isTidy(string s)
{
	if (s.length() == 1)
		return true;
	
	for (int i = 0; i < s.length() - 1; i++)
		if (s[i] > s[i + 1])
			return false;

	return true;

}

string subTidy(string s)
{
	int i = 2;
	for (i; i <= s.length(); i++)
	{
		string t = s.substr(0, i);
		if (!isTidy(t))
			return s.substr(0, i - 1);
	}
}

string solve(string s)
{	
	if (isTidy(s))
		return s;

	string str = subTidy(s);
	str.back() -= 1;
	while (str.length() < s.length())
	{
		str += "9";
	}

	while (str.front() == '0')
		str.erase(0, 1);

	if (!isTidy(str))
		return solve(str);

	return str;
}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("output.out");

	int T;
	fin >> T;
	for (int i = 1; i <= T; i++)
	{
		string N;
		fin >> N;
		fout << "Case #" << i << ": " << solve(N) << endl;
	}
}