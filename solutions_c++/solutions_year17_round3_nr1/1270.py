#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <map>
#include <iomanip>
#include <array>
//#include <math.h>

# define M_PIl          3.141592653589793238462643383279502884L

// https://code.google.com/codejam/contest/3274486/dashboard

struct TCake
{
	long long int nRadius;
	long long int nHeight;

	long long int Mul() const
	{
		return nRadius*nHeight;
	}

	bool operator < (const TCake& rhs)
	{
		auto nDiff = nRadius*nHeight - rhs.nRadius*rhs.nHeight;
		if (nDiff == 0)
			return nRadius > rhs.nRadius;
		
		return nDiff > 0;
	}
};

struct CTest
{
	int nTotalPancakes;
	int nStackSize;
	std::vector<TCake> arrCakes;

	void Read()
	{
		std::cin >> nTotalPancakes >> nStackSize;
		arrCakes.resize(nTotalPancakes);
		for (auto & cake : arrCakes)
		{
			std::cin >> cake.nRadius >> cake.nHeight;
		}
	}

	void Print()
	{
		long double dExposed = 0;
		// try each of the bottom cakes
		for (int nCake = 0; nCake < nTotalPancakes; ++nCake)
		{
			const TCake& tBottom = arrCakes[nCake];
			std::vector<TCake> arrPossible;
			for (int iOther = 0; iOther < nTotalPancakes; ++ iOther)
			{
				if (iOther == nCake)
					continue;
				const TCake& tOther = arrCakes[iOther];
				if (tOther.nRadius <= tBottom.nRadius)
					arrPossible.push_back(tOther);
			}
			if ((int)arrPossible.size() < nStackSize-1)
				continue;
			std::sort(arrPossible.begin(), arrPossible.end());

			long long int nCurExposed = tBottom.Mul();
			for (int nUpper = 0; nUpper < nStackSize-1; ++nUpper)
			{
				nCurExposed += arrPossible[nUpper].Mul();
			}
			
			long double dCurExposed = 2.0*M_PIl*nCurExposed;
			dCurExposed += M_PIl*tBottom.nRadius*tBottom.nRadius;

			if (dCurExposed > dExposed)
				dExposed = dCurExposed;
		}
		
		assert(dExposed > 0.0);

		std::cout << std::setprecision(std::numeric_limits<long double>::digits10 + 1) << dExposed;
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
