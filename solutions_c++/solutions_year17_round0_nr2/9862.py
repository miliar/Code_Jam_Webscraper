#include <iostream>
#include <string>
#include <cstdlib>
#include <set>
#include <vector>
#include <map>
#include <list>
#include <algorithm>
#include <fstream>

using namespace std;

#define NUM_LINES_PER_TESTCASE 3
//#define _DEBUG
#define RADIX 10


ifstream infile;
string line;
char * pEnd;
map<unsigned long long, unsigned long long> cost_map;
bool encountered3 = false;
bool encountered2 = false;
bool encountered1 = false;

unsigned long long getNextNum(unsigned long long num_temp)
{
	unsigned int remainder = 0;
	unsigned int count = 0;
	unsigned long long next_num;
	list<unsigned int> digits_list;

#ifdef _DEBUG
	cout << "List size = " << digits_list.size() << endl;
#endif
	while (num_temp > 0)
	{
		remainder = num_temp % 10;
		num_temp = num_temp / 10;
		digits_list.push_front(remainder);

#ifdef _DEBUG
		cout << "Push " << remainder << endl;
#endif
		count++;
	}

	// we have the number in the list
	// If there is a break in pattern then decrease that digit by 1 and make rest of the following digits 9
	//	For example, 718990, The first digit changes to 6 and rest of the following digits will be 9
	std::vector<unsigned int> digits_vec(digits_list.begin(), digits_list.end());
	string str;
	bool patternBreak = false;
#ifdef _DEBUG
	cout << "Vector Size = " << digits_vec.size() << endl;
#endif
	for (unsigned int i = 0; i < digits_vec.size(); i++)
	{
		if (patternBreak) {
			digits_vec[i] = 9;
		}
		if (!patternBreak && digits_vec[i] > 0 && i < digits_vec.size()-1 && digits_vec[i + 1] < digits_vec[i])
		{
			// The pattern is breaked here
			digits_vec[i] = digits_vec[i] - 1;
			patternBreak = true;
		}
		str = str + to_string(digits_vec[i]);
#ifdef _DEBUG
		cout << "str = " << str << endl;
#endif
	}
	next_num = std::stoll(str);
	return next_num;
}

void play(char *inputfile)
{
	// This function reads the file the input and processes each test case

#ifdef _DEBUG
	cout << "\nStart reading file\n";
#endif

	infile.open(inputfile, ios::in);
	if (!infile.is_open())
	{
		cout << "Unable to open input file\n";
		exit(1);
	}

	// Read the first line containing the number of test cases
	if (!getline(infile, line))
	{
		cout << "Cannot read the first line containing the number of test cases\n";
		infile.close();
		exit(1);
	}
	pEnd = NULL;
	unsigned long long  testCasesCount = 0, nTestCases = std::strtoull(line.c_str(), &pEnd, RADIX);

	int lineCount = 0, rowNumber = 0;
	int column = 0, position = 0, emptyCount = 0;
	ofstream outfile("output.txt", ios::out);
	unsigned long long num = 0, num_temp = 0, next_num = 0;
	bool satisfies = false;
	unsigned int remainder, previous_remainder;

	// Start the testcases
	while (getline(infile, line))
	{
		testCasesCount++;
		if (testCasesCount > nTestCases)
		{
			cout << "Done with All the test cases\nExiting....\n";
			break;
		}


		// First line in each test case is an integer
		num = std::strtoull(line.c_str(), &pEnd, RADIX);

#ifdef _DEBUG
		cout << "\nTest Case # " << testCasesCount << " : The number = " << num << endl;
#endif
		// Count from backward
		while (num > 0)
		{
			num_temp = num;
			previous_remainder = 10;
			bool satisfies = true;
			while (num_temp > 0) {
				remainder = num_temp % 10;
				if (remainder <= previous_remainder) {
					num_temp = num_temp / 10;
					previous_remainder = remainder;
				}
				else {
					satisfies = false;
					break;
				}
			}
			if (satisfies == true) {
				outfile << "Case #" << testCasesCount << ": " << num << endl;
#ifdef _DEBUG
				cout << "Case #" << testCasesCount << ": " << num << endl;
#endif
				break;
			}
			num = getNextNum(num);
#ifdef _DEBUG
			cout << "The next number is " << num << endl;
#endif
		}
	}	// end of While(getline())

		// Close the files
	infile.close();
	outfile.close();
}

int main(int argc, char *argv[])
{
	if (argc < 2)
	{
		cout << "Please provide the name of the input file. Format : \n./go input.txt\n";
		exit(1);
	}
	play(argv[1]);
	return 0;
}
