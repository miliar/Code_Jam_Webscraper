#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

string solve(string input)
{
	if (input.size() == 1) return input;
	string output = "";

	bool zero = false;
	int i;
	for (i = input.size() - 1; i >= 0; i--)
	{
		if (input[i] == '0')
		{
			zero = true;
		}
		if (zero && input[i] != '0')
		{
			break;
		}
	}

	//i should be 0 or where 0s end.
	if (zero)
	{
		int zIndex = i;
		for (i = 0; i < zIndex; i++)
		{
			output += input[i];
		}
		if (input[i] > '1')
			output += input[i] - 1;
		else
		{
			output = "";
			for (size_t i = 0; i < input.size() - 1; i++)
			{
				output += '9';
			}
			return output;
		}
		for (; i < input.size() - 1; i++)
		{
			output += '9';
		}
		input = output;
	}

	output = "";
	bool fd = false;
	for (i = 1; i < input.size(); i++)
	{
		if (input[i] < input[i - 1])
		{
			fd = true;
			break;
		}
		output += input[i - 1];
	}
	if (fd) output += input[i - 1] - 1;
	else output += input[i - 1];
	for (; i < input.size(); i++)
	{
		output += '9';
	}

	return output;
}

void main() {
	int t;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		string input;
		cin >> input;
		auto solution = solve(input);
		while (true)
		{
			if (solve(solution) == solution) break;
			solution = solve(solution);
		}

		cout << "Case #" << i << ": " << solution << endl;
	}
}