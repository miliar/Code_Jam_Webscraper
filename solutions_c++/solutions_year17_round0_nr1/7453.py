#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <fstream>

using namespace std;

string NoLeadingZeroes(string s)
{
	int k = 0;
	while (k < s.length() && s[k] == '0')
		k++;
	return s.substr(k);
}

int main()
{
	ifstream infile;
	infile.open("A-large.in");
	ofstream outfile;
	outfile.open("output1.txt");
	int t;
	int num;
	int cnt;
	string str;
	//ostringstream convert;
	infile >> t;
	for (int i = 0; i < t; i++)
	{
		infile >> str >> num;
		cnt = 0;
		//convert << num;
		//str = convert.str();
		//convert.str("");
		//convert.clear();
		int k = 0;
		while (k < str.length() - num + 1)
		{
			if (str[k] == '-')
			{
				for (int j = 0; j < num; j++)
				{
					if (str[j + k] == '-')str[j + k] = '+';
					else str[j + k] = '-';
				}
				cnt++;
			}
			k++;
		}
		while (k < str.length())
		{
			if (str[k] == '-')
			{
				outfile << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
				break;
			}
			k++;
		}
		if (k == str.length())
			outfile << "Case #" << i + 1 << ": " << cnt << endl;
	}
	outfile.close();
	return 0;
}