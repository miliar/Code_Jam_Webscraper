#include<iostream>
#include<string>
#include<fstream>
using namespace std;
string s;
int main()
{
	ifstream input;
	input.open("B-large.in");
	ofstream output;
	output.open("B_output.txt");
	int t;

	input >> t;
	for (int test = 0; test < t; test++)
	{

		input >> s;
		for (int i = 0; i<s.size() - 1; i++)
		{
			if (s[i] == '0'){
				s.erase(0, 1);
				continue;
			}
			if (s[i]>s[i + 1])
			{
				s[i]--;
				for (int j = i + 1; j < s.size(); j++)
				{
					s[j] = '9';
				}
				i = -1;
			}
		}
		cout << "Case #" << test + 1 << ": ";
		cout << s;
		if (test != t - 1)cout << "\n";

		output << "Case #" << test + 1 << ": ";
		output << s;
		if (test != t - 1)output << "\n";
	}
}