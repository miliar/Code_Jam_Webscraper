// A.cpp : main project file.

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


int main(int argc, char * argv)
{
	fstream In("A-large.in", ios::in);
	fstream Out("A-large.out", ios::out);
	int cases;

	In >> cases;

	for (int h = 0; h < cases; h++)
	{
		string s;
		int N;
		In >> s >> N;
		int flips = 0;
		for (int i = 0; i + N <= s.size(); i++)
			if (s[i] == '-')
			{
				flips++;
				for (int j = 0; j < N; j++)
					if (s[i + j] == '-')
						s[i + j] = '+';
					else
						s[i + j] = '-';

			}
		
		Out << "Case #" << (h + 1) << ": ";
		bool flag = true;
		for (int i = 0; i < s.size(); i++)
			if (s[i] == '-')
			{
				flag = false;
				break;
			}
		if (flag)
			Out << flips << endl;
		else
			Out << "IMPOSSIBLE" << endl;
	}
	In.close();
	Out.close();
	return 0;
}
