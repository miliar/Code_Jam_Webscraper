#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <map>
#include <iomanip>
#include <array>

// https://code.google.com/codejam/contest/3274486/dashboard#s=p1

struct TActivity
{
	long int nStartMinute;
	long int nEndMinute;

	bool operator < (const TActivity& rhs)
	{
		return nStartMinute < rhs.nStartMinute;
	}

	void NextDay()
	{
		nStartMinute += 1440;
		nEndMinute += 1440;
	}
};

struct CTest
{
	int Ac, Aj;

	std::vector<TActivity> arrCam;
	std::vector<TActivity> arrJam;
	
	void Read()
	{
		std::cin >> Ac >> Aj;
		arrCam.resize(Ac);
		arrJam.resize(Aj);

		for (auto & act: arrCam)
		{
			std::cin >> act.nStartMinute >> act.nEndMinute;
		}
		std::sort(arrCam.begin(), arrCam.end());

		for (auto & act : arrJam)
		{
			std::cin >> act.nStartMinute >> act.nEndMinute;
		}
		std::sort(arrJam.begin(), arrJam.end());
	}

	// return the number of splits
	int SolveSimple(const std::vector<TActivity>& act2)
	{
		assert(act2.size() == 2);
		if (act2[1].nEndMinute - act2[0].nStartMinute <= 720)
			return 2;

		TActivity tNextDay = act2[0];
		tNextDay.NextDay();
		if (tNextDay.nEndMinute - act2[1].nStartMinute <= 720)
			return 2;

		return 4;
	}

	void Print()
	{
		if (Ac + Aj <= 2)
		{
			if (Ac == Aj || Ac + Aj < 2)
			{				
				std::cout << 2;
				return;
			}
			
			int nResult = (Ac > 0) ? SolveSimple(arrCam) : SolveSimple(arrJam);
			std::cout << nResult;
			return;
		}
		std::cout << 2;
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
		std::cout << std::endl;

	}

	return 0;
}
