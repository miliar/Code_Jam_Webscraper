// GCJ2017 - RQ P2.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using std::ifstream;
using std::ofstream;
using std::string;
using std::cout;
using std::cin;
using std::endl;
using std::vector;

vector<int> reverseVector(const vector<int>& digits)
{
	vector<int> result;
	for (int i = digits.size() - 1; i >= 0; i--)
	{
		result.push_back(digits.at(i));
	}
	return result;
}

bool isTidy(unsigned long long int number)
{
	if (number < 10)
	{
		return true;
	}
	vector<int> digits;
	unsigned long long int current = number;
	while (current)
	{
		digits.push_back(current % 10);
		current /= 10;
	}
	digits = reverseVector(digits);
	for (int i = 0; i < digits.size() - 1; i++)
	{
		if (digits.at(i) > digits.at(i + 1))
		{
			return false;
		}
	}
	return true;
}

int main()
{
	unsigned long long int a = 111111111111111110;
	ifstream inputFile;
	ofstream outputFile;

	string filename;
	cout << "Enter filename: ";
	getline(cin, filename);

	string filenameOut;
	filenameOut = filename.substr(0, filename.find('.') + 1).append("out");

	inputFile.open(filename);

	if (!inputFile)
	{
		cout << "Couldn't open input file..." << endl;
		return 1;
	}

	outputFile.open(filenameOut);

	if (!outputFile)
	{
		cout << "Couldn't open output file..." << endl;
		return 2;
	}

	int count;
	inputFile >> count;

	cout << "Values found: " << count << "." << endl;

	for (int i = 0; i < count; i++)
	{
		bool found = false;

		unsigned long long int number;
		inputFile >> number;

		outputFile << "Case #" << (i + 1) << ": ";

		for (unsigned long long int i = number; i >= 1; i--)
		{
			if (!isTidy(i))
			{
				continue;
			}
			found = true;
			outputFile << i << endl;
			break;
		}
		if (found)
		{
			continue;
		}
		else
		{
			outputFile << "1" << endl;
		}
	}

	cout << "Done. Saved to " << filenameOut << "." << endl;

    return 0;
}

