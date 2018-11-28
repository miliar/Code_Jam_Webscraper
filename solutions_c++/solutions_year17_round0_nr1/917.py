// Google Code Jam 2017 - Qualifying Round
// A

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int t;
string s;
int batch;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.txt");
	fin >> t;
	for (int h = 1; h <= t; h++)
	{
		fin >> s >> batch;
		bool possible = true;
		string diff = (s[0] == '+') ? "0" : "1";
		for (int i = 0; i < s.length() - 1; i++)
		{
			diff += (s[i] == s[i + 1]) ? "0" : "1";
		}
		diff += (s[s.length() - 1] == '+') ? "0" : "1";
		int count = 0;
		for (int i = 0; i < diff.length(); i++)
		{
			if (diff[i] == '1')
			{
				if (i < diff.length() - batch)
				{
					diff[i] = '0';
					diff[i + batch] = (diff[i + batch] == '1') ? '0' : '1';
					count++;
				}
				else
				{
					possible = false;
				}
			}
		}
		fout << "Case #" << h << ": ";
		if (possible) fout << count << endl;
		else fout << "IMPOSSIBLE" << endl;
	}
}