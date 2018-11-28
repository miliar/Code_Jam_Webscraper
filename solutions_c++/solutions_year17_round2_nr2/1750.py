#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <map>
#include <iomanip>

//https://code.google.com/codejam/contest/8294486/dashboard

#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <map>
#include <iomanip>

// https://code.google.com/codejam/contest/dashboard?c=8294486#s=p1

enum basic_shades
{
	red = 0,
	yellow = 1,
	blue = 2
};

const char cShades[] = "RYB";

struct TShade
{
	basic_shades shade;
	int count = 0;

	bool operator < (const TShade& rhs) const
	{
		return count < rhs.count;
	}

};

const char bCtypes[] = "ROYGBV";

struct CTest
{
	std::vector<TShade> arrShadeCount;
	int ROYGBV[6] = { 0 };
	int NPlaces;

	std::vector<char> arrPlaces;

	CTest()
	{
		arrShadeCount.resize(3);
		arrShadeCount[red].shade = red;
		arrShadeCount[yellow].shade = yellow;
		arrShadeCount[blue].shade = blue;
	}
	
	// Small dataset
	// O = G = V = 0. (Each unicorn has only one hair color in its mane.)
	void Read()
	{
		std::cin >> NPlaces;
		for (int nNew = 0; nNew < 6; ++nNew)
		{
			std::cin >> ROYGBV[nNew];
			if (bCtypes[nNew] == 'R')
				arrShadeCount[red].count+= ROYGBV[nNew];
			else if (bCtypes[nNew] == 'Y')
				arrShadeCount[yellow].count += ROYGBV[nNew];
			else if (bCtypes[nNew] == 'B')
				arrShadeCount[blue].count += ROYGBV[nNew];
		}

		arrPlaces.resize(NPlaces,'x');

		std::sort(arrShadeCount.begin(), arrShadeCount.end());
	}

	void Print() 
	{
		int nMax = arrShadeCount[2].count;
		int nSpaces = NPlaces / nMax;
		if (nSpaces < 2)
		{
			std::cout <<"IMPOSSIBLE" << std::endl;
			return;
		}
		// max shade
		{
			char cMax = cShades[arrShadeCount[2].shade];
			for (int nCur = 0; nCur < nMax; ++nCur)
			{
				arrPlaces[nCur * 2] = cMax;
			}
		}
		// mid
		{
			char cMid = cShades[arrShadeCount[1].shade];
			int nCount = arrShadeCount[1].count;
			//go backwards, start with the last odd
			int nLastOdd = NPlaces-1;
			if (nLastOdd % 2 == 0)
				nLastOdd--;
			for (int nCur = 0; nCur < nCount; ++nCur)
			{
				assert(arrPlaces[nLastOdd - nCur * 2] == 'x');
				arrPlaces[nLastOdd- nCur*2] = cMid;
			}
		}
		// min - fill in the missing empty places
		{
			char cMin = cShades[arrShadeCount[0].shade];
			int nCheck = 0;
			
			for (int nCur = 0; nCur < NPlaces; ++nCur)
			{
				if (arrPlaces[nCur] == 'x')
				{
					arrPlaces[nCur] = cMin;
					nCheck++;
				}
			}

			assert(nCheck == arrShadeCount[0].count);
		}
		
		for (char c : arrPlaces)
			std::cout << c;

		std::cout << std::endl;
	}
};


int main()
{

	int nTests;
	std::cin >> nTests;

	for (int nCase = 0; nCase < nTests; ++nCase)
	{
		CTest curTest;
		curTest.Read();

		std::cout << "Case #" << nCase + 1 << ": "; 
		curTest.Print();

	}

	return 0;
}



