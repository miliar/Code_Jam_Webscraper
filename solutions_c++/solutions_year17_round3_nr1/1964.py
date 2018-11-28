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
#include <list>
#include <numeric>

double PI = 3.14159265358979323846264338327950288;
int _tmain(int argc, _TCHAR* argv[])
{
	std::multimap<int, int> myMap = { { 3, 2 }, { 3, 4 }, { 1, 2 }, { 2, 2 } };
	

	int N,K;
	int T;

	std::cin >> T;

	for (unsigned int i = 0; i < T; i++)
	{
		std::cin >> N>>K;
		std::multimap<double,double> mults;
		std::vector<int> rs;
		for (unsigned int j = 0; j < N; j++)
		{
			long long R, H;

			std::cin >> R >> H;

		//	rs.push_back(R);
			long long mult = H*R;
			mults.insert({ (double)mult, R });

		}
		
	//	std::sort(rs.begin(), rs.end());
		double Max = 0;
		for (auto j = mults.rbegin(); j != mults.rend(); ++j)
		{
			auto rs = j->second;
			double SA = PI*rs* rs;
			double Sum = 0;
			int nCount = 0;
			auto mapEnd = mults.rbegin();
			bool RSAdded = false;

			Sum += SA + (2 * PI*(j->first));
			nCount++;
			while ((nCount<K) && (mapEnd != mults.rend()))
			{

				if ((mapEnd->second <= rs) && (mapEnd!=j))
				{
					Sum += 2*PI*(mapEnd->first);
					nCount++;
				}
				++mapEnd;
				
			}
			if ((Sum>Max) && (nCount==K))
			{
				Max = Sum;
			}


		}

		std::cout.precision(17);
	//	if (result ==true)
		{
			std::cout << "Case #" << i + 1 << ": " << Max<< std::endl;
		}
	//	else
		{
	//		std::cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << std::endl;
		}
	}

	return 0;
}

