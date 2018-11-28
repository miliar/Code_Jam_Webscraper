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
	infile.open("B-large.in");
	ofstream outfile;
	outfile.open("output1.txt");
	int t;
	long long num;
	string str;
	ostringstream convert;
	infile >> t;
	for (int i = 0; i < t; i++)
	{
		infile >> num;
		convert << num;
		str = convert.str();
		convert.str("");
		convert.clear();
		if (str.length() == 1)
		{
			outfile << "Case #" << i + 1 << ": " << NoLeadingZeroes(str) << endl;
			continue;
		}
		for (int j = str.length() - 1; j > 0; j--)
		{
			if (str[j] < str[j - 1])
			{
				str[j - 1]--;
				for (int k = j; k < str.length(); k++)
				{
					if (str[k] == '9')
						break;
					else str[k] = '9';
				}
			}
		}
		outfile << "Case #" << i + 1 << ": " << NoLeadingZeroes(str) << endl;
	}
	outfile.close();
	return 0;
}