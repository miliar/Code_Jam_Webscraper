#include <fstream>
#include <unordered_set>
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <iterator>
#include <string>
using namespace std;

void substractOne(deque<char> & data, size_t pos);

void TidyNumbers(int argc, char** argv)
{
	ifstream in(argv[1]);
	ofstream out(argv[2]);

	unsigned int cases;
	in >> cases;
	istream_iterator<string> start(in), end;

	vector<string> nums(start, end);

	in.close();

	for (size_t l = 0; l < nums.size(); l++)
	{
		string str = nums[l];
		cout << str << endl;

		deque<char> digits;

		for (char c : str)
			digits.push_back(c);

		bool asc = false;

		while (!asc)
		{
			asc = true;

			for (int i = 1; i < digits.size(); ++i)
			{
				if (digits[i] < digits[i - 1])
				{
					asc = false;
					break;
				}
			}

			if (asc)
				break;

			for (int i = digits.size() - 1; i > 0; --i)
			{
				if (digits[i - 1] > digits[i])
					for (int j = i; j < digits.size(); ++j)
						digits[j] = '0';
			}

			substractOne(digits, digits.size() - 1);
			if (digits[0] == '0')
				digits.pop_front();

		}



		str.clear();
		for (char c : digits)
			str.push_back(c);

		cout << "Case #" << l + 1 << ": " << str << endl;
		out << "Case #" << l + 1 << ": " << str << endl;
	}
}

void substractOne(deque<char> & data, size_t pos)
{
	if (pos == 0 && data[pos] == '1')
	{
		data[pos] = '0';
		return;
	}


	if (data[pos] == '0')
	{
		substractOne(data, pos - 1);

		data[pos] = '9';
	}
	else
	{
		data[pos] -= 1;
	}



}