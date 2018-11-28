/*
ID: paradoxes
PROG: Tidy Numbers
LANG: C++
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>

using namespace std;

int T;

int charToInt(char a)
{
	return ((int)(a - '0'));
}

string tidy(string num, char limit)
{
	if (num.length() == 1)
	{
		if (charToInt(num[0]) >= charToInt(limit))
			return string(1, num[0]);
		else
			return "-1";
	}

	if (num[0] == '0')
		return "-1";
		//return tidy(num.substr(1, num.length() - 1), limit);

	string a = tidy(num.substr(1, num.length() - 1), max(num[0], limit));



	if (a != "-1")
	{
		if (num[0] < limit)
			return "-1";

		else
			return num[0] + a;
	}

	if (num[0] <= limit)
	{
		return "-1";
	}

	else if (num[0] == '1')
	{
		return string(num.length() - 1, '9');
	}

	else
	{
		return (char)(num[0] - 1) + string(num.length() - 1, '9');
	}

}

int main()
{
	ifstream Input("tidy.in");
	ofstream Output("tidy.out");

	Input >> T;

	string in;

	for (int j = 1; j <= T; j++)
	{
		Input >> in;
		
		Output << "Case #" << j << ": " << tidy(in, '0') << endl;
	}

	return 0;
}