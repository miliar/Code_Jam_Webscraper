// b-tidynumbers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>

using namespace std;

bool changeChars(char &na, char &nb)
{
	bool repeat = false;
	
	if (na > nb)
	{
		nb = '9';
		
		if (na == '0')
		{
			na = 9;
		}
		else
		{
			na--;
		}

		repeat = true;
	}
	
	return repeat;
}

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int i = 0; i < numCases; i++)
	{
		// input
		string num = "";
		cin >> num;

		// calc
		for (int j = num.size() - 2; j >= 0; j--)
		{	
			// if repeat, return on loop
			if (changeChars(num[j], num[j + 1]))
			{
				for (int k = j + 1; k < num.size(); k++)
				{
					num[k] = '9';
				}
			}
		}

		// clean
		if (num.size() > 1)
		{
			while (num[0] == '0')
			{
				num.erase(num.begin());
			};
		}

		// output
		cout << "Case #" << i + 1 << ": ";
		cout << num;

		cout << endl;
	}

	return 0;
}

