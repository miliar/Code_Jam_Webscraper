#include <iostream>
#include <vector>


// https://code.google.com/codejam/contest/dashboard?c=3264486


// LSB is at the begning
void BreakDigits(long long N, std::vector<int>& outDigits)
{
	outDigits.resize(0);
	while (N>0)
	{
		long long LSB = N%10;		
		N /= 10;
		outDigits.push_back(static_cast<int>(LSB));
	}
}

long long BuildNumber(const std::vector<int>& arrDigits)
{
	long long N = 0;
	long long nPow = 1;
	for (unsigned int digit = 0; digit<arrDigits.size(); ++digit)
	{
		N += nPow*(long long)arrDigits[digit];
		nPow *= 10;
	}

	return N;
}

bool IsTidy(long long N)
{
	long long prevLSB = 9;
	while (N>0)
	{
		long long LSB = N%10;
		if (LSB>prevLSB)
			return false;
		prevLSB = LSB;
		N /= 10;
	}
	return true;
}

long long LastTidy(long long N)
{
	if (N<=9)
		return N;
	std::vector<int> arrDigits;
	BreakDigits(N, arrDigits);
	// start with the most significant bit
	unsigned int nStopPos = arrDigits.size();
	if (arrDigits.back()>1)
		nStopPos = arrDigits.size()-1;

	for (int nDigit = arrDigits.size()-1; nDigit>0; --nDigit)
	{
		// save the min position in which there is real increase (so far)
		if (arrDigits[nDigit]<arrDigits[nDigit-1])
			nStopPos = nDigit-1;
		if (arrDigits[nDigit]>arrDigits[nDigit-1])
		{
			if (nStopPos<arrDigits.size())
			{
				arrDigits[nStopPos]--;
			} else
			{				
				arrDigits.pop_back();
				nStopPos = arrDigits.size();
			}
			// set all 9 from this point to the bottom
			for (int nBottom = nStopPos-1; nBottom >=0; --nBottom)
				arrDigits[nBottom] = 9;
			
			break;
		}
	}
	// rebuild the number from vector
	return BuildNumber(arrDigits);
}

long long LastTidyNaive(long long N)
{
	while (!IsTidy(N))
	{
		N--;
	}
	return N;
}


int main()
{
	{
		// unit test
		long long nCheck = 115527;
		long long nLastTidy = LastTidy(nCheck);
		// naive algorithm
		nCheck = LastTidyNaive(nCheck);
		if (nLastTidy != nCheck)
		{			
			std::cerr << "error";
		}

		nCheck = 312;
		nLastTidy = LastTidy(nCheck);
		// naive algorithm
		nCheck = LastTidyNaive(nCheck);
		if (nLastTidy != nCheck)
		{			
			std::cerr << "error";
		}
		
	}
	int nTests;
	std::cin >> nTests;
	for (int nCase =0 ; nCase < nTests; ++nCase)
	{				
		long long N;
		std::cin >> N;
								
		std::cout<<"Case #"<<nCase+1<<": "<<LastTidy(N)<<std::endl;
								
	}

	return 0;
}
