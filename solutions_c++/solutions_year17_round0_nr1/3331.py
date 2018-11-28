// gcj1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
//#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	ifstream in("A-large.in");
	ofstream out("out.txt");
	int n;
	in >> n;
	for (int i = 0; i < n; ++i)
	{
		string s;
		int z;
		in >> s >> z;
		auto result = 0;
		for (int j = 0; j < s.size() - z + 1; ++j)
		{
			if (s[j] == '-')
			{
				result++;
				for (int c = j + 1; c < j + z; ++c)
				{
					s[c] = s[c] == '+' ? '-' : '+';
				}
			}
		}
		if (find(s.end() - z + 1, s.end(), '-') !=  s.end())
		{
			out << "Case #"<< (i+1) << ": IMPOSSIBLE" << endl;
		} 
		else
		{
			out << "Case #" << (i + 1) << ": " << result << endl;
		}

	}

    return 0;
}

