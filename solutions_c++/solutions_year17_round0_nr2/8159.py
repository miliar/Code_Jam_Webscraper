
#include "stdafx.h"
#include <iostream>
#include <string>
#include <sstream>
using namespace std;


int getlasttight2(string& s)
{
	bool haschanged = false;
	do {
		int max = s.length() - 1;
		int x = 0;
		bool isnotight = false;
		bool changefor9 = false;
		char mindigit = '9';
		
		haschanged = false;
		while ((x < max))
		{
	//		cout << x << endl;
	//		if (x == 14)
	//			cout << "near" <<endl;
			if (!changefor9)
			{
				isnotight = s.at(x) <= s.at(x + 1);
				if (mindigit > s.at(x))
					mindigit = s.at(x);
				if (!isnotight)
				{
					char inext = s.at(x + 1);
					char y = s.at(x);

					while (y > inext)
					{
						y--;
						inext = '9';
					}
					s.at(x) = y;
					s.at(x + 1) = '9';
					haschanged = true;
					changefor9 = true;
				}
			}
			else
			{

				s.at(x) = '9';
				haschanged = true;
			}
			x++;
		}
		if (changefor9)
		{
			s.at(max) = '9';
			haschanged = true;
		}
		if (s.at(0) == '0')
		{
			haschanged = true;
			s.erase(0, 1);
		}
	//	cout << "   " << s << endl;
	} while (haschanged);
	return true;
}

int main()
{
	int casecount;
	string number; 
	cin >> casecount;
	getline(cin, number);
	for (int i = 0; i < casecount; i++)
	{

		getline(cin, number);
	//	cout << number << " ";
		getlasttight2(number);
		cout << "Case #" << i+1 << ": " << number << endl;
	}
	return 0;
}