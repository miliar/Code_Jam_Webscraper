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
	static unsigned long long int num[200], val[200];
	srand(time(0));
	unsigned int cs ;
	cin >> cs;
	for (unsigned int C = 1; C <= cs; ++C)
	{

		unsigned long long int N , T;
		cin >> N >> T ;

		unsigned long long int *pnum = num, *pval = val, *tnum, *tval;
		for (auto it = num, _it = num+200; it<_it; ++it) *it=0;
		for (auto it = val, _it = val+200; it<_it; ++it) *it=0;

		*pnum = N;
		*pval = 1;
		unsigned long long int tt = 1, smx, smn;
		smx = smn = (*pnum-1)/2; if (*pnum%2==0) ++smx;
		//cerr << N << " " << T << " " << endl;
		//cerr << *pnum << " " << smx << " " << smn << " ";
		//cerr << *pnum << " " << *pval << " " << " " << tt << " "<< endl;
		for(;tt<T;)
		{
			for(tnum = pnum+1; *tnum > smx; ++tnum);
			tval = pval + (tnum-pnum);
			if(*tnum == 0) *tnum = smx;
			*tval += *pval;
			if (smx > smn)
			{
				++tnum; ++tval;
				if(*tnum == 0) *tnum = smn;
			}
			*tval += *pval;
			++pnum; ++pval; tt+=*pval;
			smx = smn = (*pnum-1)/2; if (*pnum%2==0) ++smx;
			//cerr << *pnum << " " << smx << " " << smn << " ";
			//cerr << *pnum << " " << *pval << " " << tt << endl;
		}
		//cerr << *pnum << " " << smx << " " << smn << " ";
		//cerr << *pnum << " " << *pval << " " << tt << endl;
		//cerr << "**********" << endl;
		cout << "Case #" << C << ": " << smx << " " << smn << endl;
		//cerr << "**********" << endl;
		//cerr << endl << endl << endl;
	}

	return 0;
}
