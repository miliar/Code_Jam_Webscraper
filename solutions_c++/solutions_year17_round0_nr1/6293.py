#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

//greedy but works :)
string solve(string s, int k)
{
	int steps = 0;
	int length = s.length();
	if (s.find('-') == string::npos)
		return "0";
	int i = 0;
	while(i != string::npos && i <= length - k)
	{
		string seq = s.substr(i, k);
		if (seq.find('-') == string::npos)
			i += k;
		else if(s.at(i) == '-')
		{
			steps++;
			for (int j = i; j < i + k; j++)
			{
				if (s.at(j) == '-')
					s.at(j) = '+';
				else
					s.at(j) = '-';
			}
		}
		i = s.find('-', i);
	}

	if (s.find('-') == string::npos)
		return to_string(steps);
	else
		return "IMPOSSIBLE";
}

int main()
{
	ifstream input;
	string iname;
	cin >> iname;

	input.open(iname.c_str());

	string line;
	getline(input, line);

	ofstream output;
	output.open("output.txt");

	int lines = atoi(line.c_str());

	for (int i = 0; i < lines; i++)
	{
		getline(input, line);
		stringstream ss(line);
		string seq; int k;

		ss >> seq >> k;
		output << "Case #" << i + 1 << ": " << solve(seq, k) << endl;
	}

	return 0;
}