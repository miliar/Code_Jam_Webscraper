#include <iostream>
#include <fstream>
#include <string>

using namespace std;

unsigned long long findLastTidy(unsigned long long N)
{
	if (N < 10)
	{
		return N;
	}
	string s = to_string(N);
	for (int i = 0; i < s.size()-1; ++i)
	{
		if (s.at(i) > s.at(i+1))
		{
			N = N - stoll(s.substr(i+1)) - 1;
			s = to_string(N);
			for (int j = i; j > 0; --j)
			{
				if (s.at(j - 1) > s.at(j))
				{
					N = N - stoll(s.substr(j)) - 1;
					s = to_string(N);
				}
			}
		}
	}
	return N;
}

int main(){ 
	ifstream input;
	input.open("input.txt");
	ofstream output;
	output.open("output.txt");
	if (!output.is_open())
	{
		cout << "Cannot open output file!" << endl;
		return 1;
	}
	if (input.is_open())
	{
		string line;
		getline(input, line);
		int cases = stoi(line);
		for (int c = 1; c <= cases; ++c)
		{
			if (!getline(input, line))
			{
				cout << "Cannot find further test cases!" << endl;
				return 1;
			}
			unsigned long long tidy = findLastTidy(stoll(line));
			output << "Case #" << c << ": " << tidy << endl;
		}
	}
	else
	{
		cout << "Cannot read input file!" << endl;
	}
	input.close();
	output.close();
	return 0;
}