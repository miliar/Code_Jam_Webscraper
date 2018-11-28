#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

typedef unsigned long long ull;

ull last_tidy(ull n)
{
	string digits = to_string(n);
	int unary_len = 1;
	int down_pos = 0;
	for (int i = 0; i < digits.size() - 1; i++)
	{
		if (digits[i] > digits[i + 1])
		{
			down_pos = i - unary_len + 1;
			digits[down_pos]--;
			for (int j = down_pos + 1; j < digits.size(); j++)
			{
				digits[j] = '9';
			}
			if (digits[0] == '0')
			{
				digits.erase(0, 1);
			}
			// cout << digits << endl;
			return stoull(digits);
		}
		if (digits[i] == digits[i + 1])
		{
			unary_len++;
		}
		else
		{
			unary_len = 1;
		}
	}
	return n;
}

int main(int argc, char const *argv[])
{
	string sizes[2] = {"-small", "-large"};

	char prob_num = 'B';
	string data_size = sizes[1];

	string in_name = prob_num + data_size + ".in";
	string out_name = prob_num + data_size + ".out";

	ifstream infile(in_name.c_str());
	string line;
	int T;
	infile >> T;
	getline(infile, line);

	ofstream outfile(out_name.c_str());
	ull N;
	for (int i = 0; i < T; i++)
	{
		infile >> N;
		// cout << K << endl;
		outfile << "Case #" << i + 1 << ": ";
		outfile << last_tidy(N) << endl;
	}
	return 0;
}