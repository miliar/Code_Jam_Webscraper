#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int moves(string s, int k)
{
	int found = s.find('-');
	int pos;
	int flips = 0;
	bool cando = true;
	while (found != string::npos)
	{		
		for (int i = 0; i < k; i++)
		{
			pos = found + i;
			if (pos >= s.size())
			{
				cando = false;
				break;
			}
			if (s[pos] == '+')
			{
				s[pos] = '-';
			}
			else
			{
				s[pos] = '+';
			}
		}
		if (!cando)
		{
			return -1;
		}
		flips++;
		found = s.find('-');
		// cout << s <<endl;
	}
	return flips;
}

int main(int argc, char const *argv[])
{
	string sizes[2] = {"-small", "-large"};

	char prob_num = 'A';
	string data_size = sizes[1];

	string in_name = prob_num + data_size + ".in";
	string out_name = prob_num + data_size + ".out";

	ifstream infile(in_name.c_str());
	string line;
	int T;
	infile >> T;
	getline(infile, line);

	ofstream outfile(out_name.c_str());
	int K;
	for (int i = 0; i < T; i++)
	{
		getline(infile, line, ' ');
		infile >> K;
		// cout << K << endl;
		outfile << "Case #" << i + 1 << ": ";
		int result = moves(line, K);
		if (result < 0)
		{
			outfile << "IMPOSSIBLE" << endl;
		}
		else
		{
			outfile << result << endl;
		}
	}
	return 0;
}