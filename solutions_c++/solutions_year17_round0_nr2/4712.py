#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <array>
#include <vector>
#include <algorithm>
#include <numeric>
#include <ctime>
#include <limits>
#include <cmath>
#include <cassert>

using namespace std;


int main(int argc, char** argv)
{
	static int num[24];
	srand(time(0));
	unsigned int cs ;
	cin >> cs;
	for (unsigned int C = 1; C <= cs; ++C)
	{
		for (int * tt = num, *_tt = num+24; tt<_tt; ++tt) *tt=0;
		unsigned long long int N;
		cin >> N;
		*num=9;
		int * it = num+1;
		for(; N > 0;++it)
		{
			*it = N%10;
			N/=10;
		}
		--it;
		//for (auto tt = it; tt>= num; --tt) cerr << *tt; cerr << endl;
		int*jt=it-1;
		while(jt>num)
		{
			//cerr << "  cc " <<*(jt+1) << *jt << endl;
			if(*jt<*(jt+1)) break;
			--jt;
		}
		if (jt > num)
		{
			while(jt<it)
			{
				//cerr << "  rr " <<*(jt+1) << *jt ;
				if(*jt>=*(jt+1)) break;
				++jt; --(*jt);
				//cerr << "  to " <<*jt << *(jt-1) << endl;
			}
			//cerr << endl;
			--jt;
			while(jt>num) *(jt--)=9;
			// */
		}
		while(*it==0)--it;
		cout << "Case #" << C << ": " ;
		for (auto tt = it; tt> num; --tt) cout << *tt;
		cout << endl;

	}

	return 0;
}
