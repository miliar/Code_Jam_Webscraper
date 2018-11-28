// QuestionA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<vector>
#include <string>
#include <map>
#include <set>
#include <fstream>
#include <iostream>
#include <algorithm>


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
	std::map<int, int> map1 = { { 1, 2 }, { 2, 1 }, { 3, 1 }, { 5, 2 }, { 4, 1 } };
	map1[1]++;
	map1[0]++;
	auto start = map1.begin();
	map1.erase(1);
	auto start1 = map1.begin();
	auto rebeg = map1.end();
	rebeg--;
	std::string s;
	long long N;
	int T, K;
	std::cin >> T;

	for (unsigned int i = 0; i < T; i++)
	{
		int L = 0;
		int R = 0;
		std::cin >> N>>K;
		std::map<long long, int> els;
		if (N >0)
		{
			els.insert({ N , 1 });
		}

		for (unsigned int j = 0; j < K; j++)
		{
			if (els.size()==0)
			{
				break;
			}
			auto rebeg1 = els.end();
			rebeg1--;
			long long space = rebeg1->first;
			if (rebeg1->second == 1)
			{
				els.erase(rebeg1);
			}
			else
			{
				rebeg1->second--;
			}
			if ((space-1)%2==0)
			{
				L = space / 2;
				R = space / 2;
			}
			else
			{
				L = (space - 2) / 2;
				R = space-1-L;
			}
			if (L!=0) els[L]++;
			if (R!=0) els[R]++;
			
		}
		int final;

		int Ltrue = std::min(L, R);
		int Rtrue = std::max(L, R);
	//	if (result ==true)
		{
			std::cout << "Case #" << i + 1 << ": " << Rtrue << " " << Ltrue << std::endl;
		}
	//	else
		{
	//		std::cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << std::endl;
		}
	}

	return 0;
}

