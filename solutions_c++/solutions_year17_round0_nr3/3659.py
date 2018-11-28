// solve.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		__int64 n, k;
		cin >> n >> k;
		if (n == k)cout << "Case #" << i << ": 0 0" << endl;
		else
		{
			map<__int64, __int64> m;
			m[n]=1;
			__int64 ppl_enter = 0;
			for (;;)
			{
				auto maxleft = *(m.rbegin());
				if (maxleft.second + ppl_enter < k)
				{
					if (maxleft.first % 2==0)
					{
						m[maxleft.first >> 1] += maxleft.second;
						m[(maxleft.first >> 1)-1] += maxleft.second;
					}
					else
					{
						m[maxleft.first >> 1] += (maxleft.second<<1);
					}
					m.erase(--m.end());
					ppl_enter += maxleft.second;
				}
				else
				{
					if (maxleft.first % 2 == 0)
						cout << "Case #" << i << ": " << (maxleft.first >> 1) << " " << (maxleft.first >> 1)-1 << endl;
					else
						cout << "Case #" << i << ": " << (maxleft.first >> 1) << " " << (maxleft.first >> 1) << endl;
					break;
				}
			}
		}
	}



    return 0;
}

