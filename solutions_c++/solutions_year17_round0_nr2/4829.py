/*
Problem B. Tidy Numbers
Confused? Read the quick-start guide.
Small input
5 points
Solve B-small
You may try multiple times, with penalties for wrong submissions.
Large input
15 points
You must solve the small input first.
You have 8 minutes to solve 1 input file. (Judged after contest.)
Problem

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with a single integer N, the last number counted by Tatiana.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.

Limits

1 ? T ? 100.
Small dataset

1 ? N ? 1000.
Large dataset

1 ? N ? 1018.
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


*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <array>
#include <queue>
#include <algorithm>
#include <sstream>
#include <array>
#include <stack> 
#include <tuple>
#include <assert.h>
#include <bitset>
#include <string.h>
#include <iomanip>

// #define SHOW
// #define TIME
#ifdef TIME
//#include <ctime>
#endif // TIME
// using ordered map
#include <map>
#include <set>
#include <unordered_map>

using namespace std;

int tidyUp(vector<int> &number)
{
	int len = (int)number.size(); 
	int idx = 0; 
	while (idx + 1 < len && number[idx] <= number[idx + 1])
		idx++; 
	return idx;
}

void tidyNumber(int caseNumber )
{
	string inp;
	cin >> inp;
	int len = (int)inp.length();
	vector<int> number(len);

	for (int i = 0; i < len; i++)
	{
		number[i] = inp[i] - '0';
	}
	int idx = tidyUp(number);
	vector<int> output(number);
	if (idx < len - 1)
	{
		// Decrease the number, till it is still tidy. 
		bool bDone = false; 
		while (!bDone)
		{
			output[idx]--; 
			if (idx == 0)
				bDone = true; // always succeed if first digit has been decreased. 
			else
			{
				if (output[idx - 1] <= output[idx])
					bDone = true; // after decrease, it is a tidy number. 
				else
				{
					if (output[idx] < 0)
						idx--;
				}
			}
		}

		int lastNumber = 9;
		while (++idx < len)
		{
			output[idx] = lastNumber; 
		}
	}
	cout << "Case #" << caseNumber << ": ";
	for (int i = 0; i < len; i++)
	{
		if (i > 0 || output[i] != 0)
		{
			cout << output[i];
		}
	}
	cout << endl; 
}

int main() {
#ifdef TIME
	auto t1 = clock();
#endif // TIME
	int numCases;
	cin >> numCases;
	for (int i = 1; i <= numCases; i++)
		tidyNumber(i);

	return 0;
}