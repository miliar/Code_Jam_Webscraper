/*
Problem

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with a single integer N, the last number counted by Tatiana.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.

Limits

1 ≤ T ≤ 100.
Small dataset

1 ≤ N ≤ 1000.
Large dataset

1 ≤ N ≤ 1018.
Sample


Input

Output

4
132
1000
7
111111111111111110

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

Note that the last sample case would not appear in the Small dataset.
*/

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <map>
#include <vector>

using namespace std;

//void ReturnStrings(string inputString, vector<string> & v_strSubStrings)
//{
//	char *ptr_StringStream = NULL;
//	char *ptr_NextStringStream = NULL;
//	char sData[10000] = "\0";
//	sprintf_s(sData, "%s", inputString.c_str());
//	ptr_StringStream = strtok_s(sData, " ", &ptr_NextStringStream);
//	while (ptr_StringStream != NULL)
//	{
//		v_strSubStrings.push_back(ptr_StringStream);
//		if (ptr_StringStream != NULL)
//			ptr_StringStream = strtok_s(NULL, " ", &ptr_NextStringStream);
//	}
//}

int CheckForImpossibility(string flipString, unsigned int index)
{
	for (unsigned int index1 = index; index1 < flipString.length(); index1++)
	{
		if (flipString.at(index1) == '-')
			return 0;
	}
	return 1;
}

int main()
{
	vector<string> lines;
	ifstream readFile("input.txt");
	if (readFile.is_open())
	{
		string line;
		while (getline(readFile, line))
		{
			lines.push_back(line);
		}
	}
	else
	{
		cout << "\n Couldn't open file for reading test cases" << endl;
	}

	int numCases = atoi(lines[0].c_str());
	int lineIndex = 0;
	vector<string> results;
	for (int caseIndex = 1; caseIndex <= numCases; caseIndex++)
	{
		unsigned int count = 0;
		string inputs = lines[++lineIndex];
		if (inputs.length() == 1)
		{
			string finalResult = "Case #" + to_string(caseIndex) + ": " + inputs;
			results.push_back(finalResult);
			continue;
		}
		string resultantString;
		__int64 lastNumber = atoll(inputs.c_str());
		bool bFoundTidyNumber = false;
		for (__int64 index = lastNumber; index > 0; index--)
		{
			string tempValue = to_string(index);
			if (tempValue.length() == 1)
			{
				string finalResult = "Case #" + to_string(caseIndex) + ": " + tempValue;
				results.push_back(finalResult);
				break;
			}
			for (unsigned int innerIndex = 0; innerIndex < tempValue.length() - 1; innerIndex++)
			{
				char value1 = tempValue.at(innerIndex);
				char value2 = tempValue.at(innerIndex +1);
				int firstNumber = value1 - '0';
				int nextNumber = value2 - '0';
				if (firstNumber <= nextNumber)
				{
					if (innerIndex == tempValue.length() - 2) 
					{
						resultantString.append(to_string(firstNumber));
						resultantString.append(to_string(nextNumber));
						string finalResult = "Case #" + to_string(caseIndex) + ": " + resultantString;
						results.push_back(finalResult);
						bFoundTidyNumber = true;
						break;
					}
					resultantString.append(to_string(firstNumber));
				}
				else
				{
					//Number not tidy
					resultantString.clear();
					break;
				}
			}
			if (bFoundTidyNumber)
				break;
		}

	}

	ofstream writeFile("output.txt");
	if (writeFile.is_open())
	{
		for (unsigned int index = 0; index < results.size(); index++)
		{
			writeFile << results[index] << "\n";
		}
	}
	else
	{
		cout << "\n Couldn't open file for writing results" << endl;
	}

	return 0;
}