
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>

using namespace std;

string solve(string number)
{
	char* arry = new char[number.size() + 1];
	arry[number.size()] = 0;
	int count = number.size();
	for (int i = 0; i < count; i++)
	{
		arry[i] = number[i];
	}
	// Find first digit that goes down
	bool didChange = true;
	while (didChange)
	{
		didChange = false;
		for (int i = 0; i < count - 1; i++)
		{
			if (arry[i] > arry[i + 1])
			{
				// bump higher order digit down by one and set all to nines.
				arry[i] --;
				for (int j = i + 1; j < count; j++)
				{
					arry[j] = '9';
				}
				didChange = true;
				continue;
			}
		}
	}
	string result = arry;
	if (arry[0] == '0')
	{
		result = &(arry[1]);
	}
	delete arry;
	return result;
}

void main()
{
	ifstream in = ifstream("B-large.in");
	ofstream out = ofstream("B-large.out");

	int numberOfCases;

	in >> numberOfCases;

	for (int i = 0; i < numberOfCases; i++)
	{
		string number;
		in >> number;

		string result = solve(number);
		cout << "Case #" << i + 1 << ": " << result << endl;
		out << "Case #" << i + 1 << ": " << result << endl;
	}

	in.close();
	out.close();
}


