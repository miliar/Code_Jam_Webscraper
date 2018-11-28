#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int doPancake(std::vector<uint8_t>& pks, int k)
{
	int numFlips = 0;
	if(pks.size() < k)
		return 0;
	
	for(unsigned i=0;i<=pks.size()-k;i++)
	{
		if(pks[i] == 1)
			continue;
		for(int j=0;j<k;j++)
			pks[i+j] ^= 1;
		numFlips++;
	}
	return numFlips;
}

int main(int argc, char* argv[])
{
	ifstream f(argv[1]);
	int numTests;
	f >> numTests;
	for(int i=0;i<numTests;i++)
	{
		std::string tmp;
		f >> tmp;
		std::vector<uint8_t> pks;
		for(char c: tmp)
		{
			if(c == '+')
				pks.push_back(1);
			else if(c == '-')
				pks.push_back(0);
		}
		int k;
		f >> k;
		int ret = doPancake(pks, k);
		for(unsigned i=0;i<pks.size();i++)
		{
			if(pks[i] == 0)
			{
				ret = -1;
				break;
			}
		}
		std::cout << "Case #" << (i+1) << ": ";
		if(ret == -1)
			std::cout << "IMPOSSIBLE\n";
		else
			std::cout << ret << "\n";
	}
	return 0;
}
