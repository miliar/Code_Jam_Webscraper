#include <fstream>
#include <iostream>
#include <string>

using namespace std;

string switchsubset(string s, int firstPos, int len)
{
	for (int i = firstPos; i < firstPos + len; i++)
	{
		if (s[i] == '-')
		{
			s[i] = '+';
		}
		else
		{
			s[i] = '-';
		}
	}

	return s;
}

bool result(string s)
{
	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] == '-')
		{
			return false;
		}
	}

	return true;

	
}

int main()
{
	ofstream fout;
	ifstream fin;
	fout.open("output.txt");
	fin.open("A-large.in");
	int T;
	fin >> T;
	for (int t = 0; t < T; t++)
	{
		
		string s;
		fin >> s;
		int K;
		fin >> K;
		int res = 0;
		for (int i = 0; i < s.size() - K + 1; i++)
		{
			if (s[i] == '-')
			{
				s = switchsubset(s, i, K);
				res++;
			}
		}

		fout << "Case #" << t + 1 << ": ";
		if (result(s))
			fout << res;
		else
			fout << "IMPOSSIBLE";
		fout << endl;
	}

	return 0;
}