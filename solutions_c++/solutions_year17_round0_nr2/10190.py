#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

bool debug()
{
	return true;
}

bool is_tidy(const string& input)
{
	if (input.size() == 1)
		return true;

	for (size_t i = 1; i < input.size(); i++)
	{
		if (input[i] < input[i - 1])
			return false;
	}

	return true;
}

string trim_left_zeroes(const string& input)
{
	if (input.size() <= 1)
		return input;

	int i = 0;
	for (i = 0; i < input.size() - 2; i++)
	{
		if (input[i] != '0')
			break;
	}

	return input.substr(i);
}

string run_test(const string& input)
{
	string result = input;

	if (is_tidy(input))
	{
		return input;
	}

	for (int i = result.size() - 1; i > 0; i--)
	{
		if (result[i] < result[i - 1])
		{
			for (int j = i; j < result.size(); j++)
				result[j] = '9';
			for (int j = i - 1; j >= 0; j--)
			{
				if (result[j] == '0')
				{
					result[j] = '9';
				}
				else
				{
					result[j]--;
					break;
				}
			}
		}
		if (is_tidy(result))
			break;
	}
	return trim_left_zeroes(result);
}

int main()
{
	//string sample = "4\n132\n1000\r\n7\n111111111111111110";
	//istringstream is(sample);

	ifstream is("input.txt");
	int test_cases = 0;
	is >> test_cases;
	for (int i = 0; i < test_cases; i++)
	{
		string test;
		is >> test;
		string result = run_test(test);
		cout << "Case #" << (i + 1) << ": " << result << endl;
	}

	return 0;
}