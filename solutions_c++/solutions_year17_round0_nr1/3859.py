// QuestionA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<vector>
#include <string>
#include <map>
#include <set>
#include <fstream>
#include <iostream>


void flip(char& b)
{
	if (b == '+')
	{
		b='-';
	}
	else
	{
		b= '+';
	}
}
int _tmain(int argc, _TCHAR* argv[])
{
	std::string s;
	int T,K;
	std::cin >> T;
	for (unsigned int i = 0; i < T; i++)
	{
		std::cin >> s >> K;
		unsigned int count = 0;
		for (unsigned int p = 0; p < s.size()-K+1; p++)
		{
			if (s[p] == '-')
			{
				count++;
				for (unsigned int flips = 0; flips < K; flips++)
				{
					flip(s[p + flips]);
				}

			}
		}
		bool result = true;
		for (unsigned int p = 0; p < s.size(); p++)
		{
			if (s[p] == '-')
			{
				result = false;
			}
		}
		if (result ==true)
		{
			std::cout << "Case #" << i + 1 << ": " << count << std::endl;
		}
		else
		{
			std::cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << std::endl;
		}
	}

	return 0;
}

