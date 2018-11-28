// QuestionA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<vector>
#include <string>
#include <map>
#include <set>
#include <fstream>
#include <iostream>


bool inorder(long long numb)
{
	bool result = true;
	long long rem = numb;
	if (numb < 10) return true;
	while (rem>9)
	{
		int lastdigit = rem % 10;
		int firstdigit = (rem / 10) % 10;
		if (lastdigit<firstdigit)
		{
			result = false;
		}
		rem = rem / 10;
	}
	return result;
}
long long pow10(long long n, unsigned int exp)
{
	
	for (unsigned int t = 0; t < exp; t++)
	{
		n = n * 10;
	}
	return n;

}
int _tmain(int argc, _TCHAR* argv[])
{
	bool ans1 = inorder(1239);
	bool ans2 = inorder(1231);
	char nums[11] = { '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
	std::string s;
	long long N;
	int T;
	std::cin >> T;
	for (unsigned int i = 0; i < T; i++)
	{
		std::cin >> N;
		long long rem = N;
		long long final=0;
		unsigned int posfactor = 0;
		while ( rem>0)
		{
			int lastdigit = rem % 10;
			if (inorder(rem))
			{
				final += pow10(rem, posfactor);
				break;
			}
			else
			{
				rem = rem - 1 - lastdigit;
				final += pow10(9, posfactor);
			}


			posfactor += 1;
			rem = rem / 10;
		}

	//	if (result ==true)
		{
			std::cout << "Case #" << i + 1 << ": " << final << std::endl;
		}
	//	else
		{
	//		std::cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << std::endl;
		}
	}

	return 0;
}

