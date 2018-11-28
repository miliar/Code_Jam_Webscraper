#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

uint64_t doNumber(uint64_t n)
{
	// Proceed backward to find the last good one
	bool isGood = true;
	do
	{
		isGood = true;
		int prevDigit = n % 10;
		uint64_t cur = n / 10;
		uint64_t mask = 1;
		while(cur)
		{
			int curDigit = cur % 10;
			cur /= 10;
			if(prevDigit < curDigit)
			{
				isGood = false;
				uint64_t badPart = n % mask;
				n-=(badPart+1);
				break;
			}
			prevDigit = curDigit;
			mask *= 10;
		}
	}
	while(!isGood);
	return n;
}

int main(int argc, char* argv[])
{
	ifstream f(argv[1]);
	int numTests;
	f >> numTests;
	for(int i=0;i<numTests;i++)
	{
		uint64_t tmp;
		f >> tmp;
		std::cerr << i << '/' << numTests << '\n';
		uint64_t ret = doNumber(tmp);
		std::cout << "Case #" << (i+1) << ": ";
		std::cout << ret << "\n";
	}
	return 0;
}
