#include <iostream>
#include <fstream>
#include <vector>
#include <assert.h>
#include <math.h>
#include <algorithm>

using namespace std;

struct Pancake
{
	double r;
	double h;
	Pancake(double r,double h):r(r),h(h)
	{
	}
	double vArea() const
	{
		return r*2.0*M_PI*h;
	}
	bool operator<(const Pancake& rhs) const
	{
		return vArea() > rhs.vArea();
	}
};

double doPcs(const std::vector<Pancake>& pcs, int startK)
{
	double outerRet = 0;
	for(int maxI=0;maxI<pcs.size();maxI++)
	{
		int K=startK;
		// Find out the p with the largest radius, that defines the horizontal surface
#if 0
		double maxR = 0;
		int maxI = -1;
		for(int i=0;i<pcs.size();i++)
		{
			if(pcs[i].r > maxR)
			{
				maxR = pcs[i].r;
				maxI = i;
			}
		}
		assert(maxI >= 0);
#endif
		// Initialize with horiz surface
		double ret = pcs[maxI].r*pcs[maxI].r*M_PI;
		// Add the vertical surface of the bottom
		ret += pcs[maxI].vArea();
		// Now we use the K-1 p with highest vertical surface. The one with the max radius will be at the bottom
		K--;
		int curI = 0;
		while(K)
		{
			if(curI == maxI)
			{
				curI++;
				continue;
			}
			// Add the vertical surface of this one
			ret += pcs[curI].vArea();
			K--;
			curI++;
		}
		if(ret > outerRet)
			outerRet = ret;
	}
	return outerRet;
}

int main(int argc, char* argv[])
{
	ifstream f(argv[1]);
	int numTests;
	f >> numTests;
	for(int i=0;i<numTests;i++)
	{
		int N, K;
		f >> N >> K;
		std::vector<Pancake> pcs;
		for(int i=0;i<N;i++)
		{
			int r,h;
			f >> r >> h;
			pcs.emplace_back(r,h);
		}
		// Order by vertical surface
		std::sort(pcs.begin(), pcs.end());
		double ret = doPcs(pcs, K);
		std::cout << "Case #" << (i+1) << ": ";
		//std::cout << ret;
		printf("%.10f",ret);
		std::cout << "\n";
	}
	return 0;
}
