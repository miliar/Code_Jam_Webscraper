// B.cpp : Defines the entry point for the console application.
//
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main(int argc, char* argv[])
{
	fstream In("b-large.in", ios::in);
	fstream Out("b-large.out", ios::out);

	int cases;

	In >> cases;

	for (int h = 0; h < cases; h++)
	{
		string s;
		In >> s;

		for (int i = s.size() - 2; i > -1; i--)
		{
			if (s[i] > s[i + 1])
			{
				s[i]--;
				for (int j = i + 1; j < s.size(); j++)
					s[j] = '9';
			}
		}

		int index = 0;
		while (s[index] == '0') index++;

		Out << "Case #" << h + 1 << ": " << s.substr(index) << endl;

	}

	In.close();
	Out.close();
	return 0;
}

