#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool isittrue(string num)
{
	for (int i = 0; i < num.length() - 1; i++)
		for (int j = i; j < num.length(); j++)
		{
			if (num[i] > num[j])
				return false;
		}

	return true;
}

string solve(string num)
{
	bool istrue = false;

		int length = num.length();
		for (int i = 0; i < length; i++)
		{
			for (int j = i + 1; j < length; j++)
			{
				if (num[i] > num[j])
				{
					while (j == 0) j--; // if there is a 0 on the previous digit.
					num[j - 1] = num[j - 1] - 1;
					for (int k = j; k < length; k++)
						num[k] = '9';

					i = -1;
					break;
				}
			}
		}
		
		while (num[0] == '0') num = num.substr(1, num.length());
		return num;
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
		output << "Case #" << i + 1 << ": " << solve(line) << endl;
		cout << "Case #" << i + 1 << ": " << solve(line) << endl;
	}

	return 0;
}