// TidyNumbers.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>

using namespace std;

int numTestCases;

int findNextNotDup(string input, char c, int size, int pos, int* countDup)
{
	if (pos < size)
	{
		if (c == input[pos])
		{
			(*countDup)++;
			return findNextNotDup(input, c, size, pos + 1, countDup);
		}
		else if (c > input[pos])
			return -1; // found lesser value
		else if (c < input[pos])
			return *countDup; // found more value
	}
	// dup until end
	return 0;
}

int main()
{
	cin >> numTestCases;

	for (int t = 1; t <= numTestCases; ++t) 
	{
		string lastNum;
		cin >> lastNum;

		string updateNum = "";
		long long int lastTidy;
		char* pEnd;
		int j;

		cout << "Case #" << t << ": ";
		int size = lastNum.size();
		if (size == 1)
		{
			cout << lastNum << endl;
			continue;
		}
			
		bool isMinusOne = false;
		for (int i = 0; i < size; ++i)
		{
			updateNum += lastNum[i];
			if (i == size - 1)
				break;

			if (lastNum[i + 1] > lastNum[i])
			{
				continue;
			}
				
			// convert value of the rest to be 0
			if (lastNum[i + 1] < lastNum[i])
			{
				for (j = i + 1; j < size; ++j)
				{
					updateNum += '0';
				}
				isMinusOne = true;
				break;
			}

			//found dup
			if (lastNum[i + 1] == lastNum[i])
			{
				int countDup = 0;
				int res = findNextNotDup(lastNum, lastNum[i], size, i + 1, &countDup);

				if (res == 0)
				{
					for (j = i + 1; j < size; ++j)
						updateNum += lastNum[j];
					break;
				}
				else if (res < 0)
				{
					for (j = i + 1; j < size; ++j)
						updateNum += '0';
					isMinusOne = true;
					break;
				}
				else
				{
					for (j = 0; j < res; ++j)
						updateNum += lastNum[i];
					i += res;
				}
			}
			
		}

		lastTidy = strtoll(updateNum.c_str(), &pEnd, 10);
		if (isMinusOne)
			--lastTidy;

		cout << lastTidy << endl;
		
	}
	return 0;
}

