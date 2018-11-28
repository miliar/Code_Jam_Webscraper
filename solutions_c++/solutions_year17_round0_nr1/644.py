#include "StdAfx.h"
#include "OversizedPancakeFlipperr.h"

#include <iostream>
#include <string>
using namespace std;



OversizedPancakeFlipperr::OversizedPancakeFlipperr(void)
{
}


OversizedPancakeFlipperr::~OversizedPancakeFlipperr(void)
{
}

int OversizedPancakeFlipperr::Solve()
{
	long t;
	cin >> t;

	for (long i = 0;i<t;i++)
	{
		string s;
		long k;
		cin >> s >> k;

		long c = 0;
		for (long p = 0;p<= s.length() - k;p++)
		{
			if (s[p]=='-')
			{
				c++;
				if (p+k > s.length())
				{
					break;
				}

				for (long h = p;h<p+k;h++)
				{
					if (s[h] == '-')
						s[h] = '+';
					else
						s[h] = '-';
					
				}
			}
		}
		bool has = false;
		for (long p = 0;p< s.length();p++)
		{
			if (s[p]=='-')
			{
				has = true;
			}
		}

		if (has)
		{
					cout << "Case #" << (i+1) << ": IMPOSSIBLE" << std::endl; 
		}
		else
		{
			cout << "Case #" << (i+1) << ": " << c << std::endl; 
		}
	}
	return 0;
}
