#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<string>

using namespace std;

int main()
{
	vector <long long unsigned int> digits;
	ifstream fin;
	fin.open("input.txt");
	ofstream fout;
	fout.open("output.txt");
	long long unsigned int t;
	fin >> t;
	for (long long unsigned int i = 0; i < t; i++)
	{
		long long unsigned int input;
		fin >> input;
		while (input > 0)
		{
			long long unsigned int a= input % 10;
			digits.push_back(a);
			input = input / 10;
		}
		reverse(digits.begin(), digits.end());
		for (int d = 0; d < 19; d++)
		{
			for (long long unsigned int j = 0; j < digits.size(); j++)
			{
				if (j < digits.size() - 1)
				{
					if (digits[j] > digits[j + 1])
					{
						digits[j] = digits[j] - 1;
						for (long long unsigned int k = j + 1; k < digits.size(); k++)
							digits[k] = 9;
					}
				}
				
			}
		}
		bool print = false;
		fout << "Case #" << i+1 << ": ";
		for (long long unsigned int k = 0; k < digits.size(); k++)
		{
			if (print == false && digits[k] != 0)
				print = true;
			if(print)
			fout << digits[k];
		}
		fout << char(10);
		digits.clear();
		digits.resize(0);
 	}

	return 0;
}
