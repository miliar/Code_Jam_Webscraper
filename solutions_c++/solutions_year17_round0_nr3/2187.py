#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

typedef unsigned long long uint64;
typedef unsigned int uint32;
typedef uint64 uint;
typedef map<uint, uint> sizeCount;


template<class T>
print_result(uint n, T res, T res2)
{
	cout << "Case #" << n << ": " << res << " " << res2 << endl;
}

int main()
{
	uint T;
	uint N, K;
	uint i,j,k;
	
	cin >> T;
	
	for (i=1; i<=T; ++i)
	{
		cin >> N >> K;
		
		uint maxD, minLast, maxLast;
		sizeCount szCount;
		bool initFlag = false;
		uint space;
		uint incr;
		// uint dbgCount = 0;
		
		szCount[N]++;
		
		for (j=0, incr=1; j<K && j<N ; j+= incr)
		{
				maxD = szCount.rbegin()->first;
				incr = szCount.rbegin()->second;
				// cout << "maxD:" << maxD << endl;
				if (maxD < 1) break; /* err */
				space = maxD - 1;
				minLast = space/2;
				maxLast = space-space/2;				 
				szCount[minLast] += incr;
			    szCount[maxLast] += incr;
				szCount.erase(maxD);
				// dbgCount++;	
		}
		
		//cout << "count :" << dbgCount << " vs " << K << " ";
		print_result(i, maxLast, minLast);		
	}
}
