#include "StdAfx.h"
#include "BathroomStalls.h"

#include <iostream>
#include <string>
#include <hash_map>

using namespace std;


BathroomStalls::BathroomStalls(void)
{
}


BathroomStalls::~BathroomStalls(void)
{
}


void BathroomStalls::Solve()
{
	long long t;
	cin >> t;

	for (long i = 0;i<t;i++)
	{
		long long N;
		cin >> N;
		long long K;
		cin >> K;
		hash_map<long long,long long> map;
		map.insert(pair<long long,long long>(N,1));
		long long cnt = K;

		while(map.size() > 0)
		{
			auto best = map.begin();
			for (auto iter = map.begin();iter != map.end();iter++)
			{
				if ((*iter).first > (*best).first)
				{
					best = iter;
				}
			}
			cnt -= (*best).second;



			long long left = (*best).first / 2;
			long long right = (*best).first - left - 1;


			if (cnt <= 0)
			{
				cout << "Case #" << (i+1) << ": " << left << " " << right << std::endl; 
				break;
			}

			if (map.find(left)== map.end())
			{
				map.insert(pair<long long,long long>(left,(*best).second));
			}
			else
			{
				map[left] += (*best).second;
			}

			if (map.find(right)== map.end())
			{
				map.insert(pair<long long,long long>(right,(*best).second));
			}
			else
			{
				map[left] += (*best).second;
			}
			map.erase(best);
		}
	}
}

