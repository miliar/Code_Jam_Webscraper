// 3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include<vector>
#include <fstream>
using namespace std;
typedef  long long ull;

bool sorting(pair<ull, ull> p1, pair<ull, ull> p2)
{
	if (p1.second - p1.first < p2.second - p2.first) return true;
	if (p1.second - p1.first > p2.second - p2.first) return false;
	return p1.first < p2.first;
}
int main()
{
	ifstream f("3_1.in");
	ofstream g("3_1.out");
	int T;
	//cin >> T;
	f >> T;
	for (int t = 1;t <= T; ++t)
	{
		ull K, N;
		f >> N >> K;
		//cin >> N >> K;
		vector<pair<ull, ull> > ints;
		ints.push_back(make_pair(1, N));
		int k = 0;
		while (k++ < K)
		{
			sort(ints.begin(), ints.end(), sorting);
			pair<ull, ull> biggest = ints[ints.size() - 1];
		
			ints.pop_back();
			ull a = biggest.first;
			ull b = biggest.second;
			if (k == K)
			{
				if ((b + a) % 2 == 0)
				{
					g << "Case #" << t << ": " << (b - a) / 2 << " " << (b - a) / 2 << endl;
				}
				else
				{
					g << "Case #" << t << ": " << (b - a) / 2 +1<< " " << (b - a) / 2 << endl;
				}
				break;
			}
			if ((b - a) % 2 == 0)
			{
				ints.push_back(make_pair(a, max(a,(a + b) / 2 - 1)));
				ints.push_back(make_pair((a + b) / 2 + 1, b));
			}
			else
			{
				ints.push_back(make_pair(a, (a + b) / 2-1));
				ints.push_back(make_pair((a + b+1) / 2, b));
			}
		}

	}
	g.close();
    return 0;
}

