/*
Problem

Last year, the Infinite House of Pancakes introduced a new kind of pancake. It has a happy face made of chocolate chips on one side (the "happy side"), and nothing on the other side (the "blank side").

You are the head cook on duty. The pancakes are cooked in a single row over a hot surface. As part of its infinite efforts to maximize efficiency, the House has recently given you an oversized pancake flipper that flips exactly K consecutive pancakes. That is, in that range of K pancakes, it changes every happy-side pancake to a blank-side pancake, and vice versa; it does not change the left-to-right order of those pancakes.

You cannot flip fewer than K pancakes at a time with the flipper, even at the ends of the row (since there are raised borders on both sides of the cooking surface). For example, you can flip the first K pancakes, but not the first K - 1 pancakes.

Your apprentice cook, who is still learning the job, just used the old-fashioned single-pancake flipper to flip some individual pancakes and then ran to the restroom with it, right before the time when customers come to visit the kitchen. You only have the oversized pancake flipper left, and you need to use it quickly to leave all the cooking pancakes happy side up, so that the customers leave feeling happy with their visit.

Given the current state of the pancakes, calculate the minimum number of uses of the oversized pancake flipper needed to leave all pancakes happy side up, or state that there is no way to do it.

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S and an integer K. S represents the row of pancakes: each of its characters is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up).

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is either IMPOSSIBLE if there is no way to get all the pancakes happy side up, or an integer representing the the minimum number of times you will need to use the oversized pancake flipper to do it.

Limits

1 ≤ T ≤ 100.
Every character in S is either + or -.
2 ≤ K ≤ length of S.
Small dataset

2 ≤ length of S ≤ 10.
Large dataset

2 ≤ length of S ≤ 1000.
Sample


Input

Output

3
---+-++- 3
+++++ 4
-+-+- 4

Case #1: 3
Case #2: 0
Case #3: IMPOSSIBLE
In Case #1, you can get all the pancakes happy side up by first flipping the leftmost 3 pancakes, getting to ++++-++-, then the rightmost 3, getting to ++++---+, and finally the 3 pancakes that remain blank side up. There are other ways to do it with 3 flips or more, but none with fewer than 3 flips.

In Case #2, all of the pancakes are already happy side up, so there is no need to flip any of them.

In Case #3, there is no way to make the second and third pancakes from the left have the same side up, because any flip flips them both. Therefore, there is no way to make all of the pancakes happy side up.
*/

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <map>
#include <vector>

using namespace std;

void ReturnStrings(string inputString, vector<string> & v_strSubStrings)
{
	char *ptr_StringStream = NULL;
	char *ptr_NextStringStream = NULL;
	char sData[10000] = "\0";
	sprintf_s(sData, "%s", inputString.c_str());
	ptr_StringStream = strtok_s(sData, " ", &ptr_NextStringStream);
	while (ptr_StringStream != NULL)
	{
		v_strSubStrings.push_back(ptr_StringStream);
		if (ptr_StringStream != NULL)
			ptr_StringStream = strtok_s(NULL, " ", &ptr_NextStringStream);
	}
}

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
		vector<string> inputStrings;
		ReturnStrings(inputs, inputStrings);
		unsigned int flipNumbers = atoi(inputStrings[1].c_str());
		string flipString = inputStrings[0];
		for (unsigned int index = 0; index < flipString.length(); index++)
		{
			if (flipString.at(index) == '+')
			{
				if (index == (flipString.length() - 1))
				{
					string finalResult = "Case #" + to_string(caseIndex) + ": " + to_string(count);
					results.push_back(finalResult);
				}
				continue;
			}
			else
			{
				if ((index + flipNumbers) > flipString.length())
				{
					int result = CheckForImpossibility(flipString, index);
					if (result == 0)
					{
						string finalResult = "Case #" + to_string(caseIndex) + ": " + "IMPOSSIBLE";
						results.push_back(finalResult);
						break;
					}
					else
					{
						string finalResult = "Case #" + to_string(caseIndex) + ": " + to_string(count);
						results.push_back(finalResult);
						continue;
					}
				}
				else
				{
					unsigned int innerIndex = 0;
					for (innerIndex = index; innerIndex < (index + flipNumbers); innerIndex++)
					{
						if (flipString.at(innerIndex) == '+')
							flipString.at(innerIndex) = '-';
						else
							flipString.at(innerIndex) = '+';
					}
					count++;
					continue;
				}
			}
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