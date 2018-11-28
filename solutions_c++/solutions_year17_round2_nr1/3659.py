#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <iomanip>
//#include <cstdio>
#include <string>
#include <array>
#include <tuple>
#include <vector>
#include <list>
#include <algorithm>
#include <numeric>
#include <ctime>
#include <limits>
#include <cmath>
#include <cassert>
// */
using namespace std;

// declare static vars


vector < tuple < unsigned long int ,unsigned long int > > R;
unsigned long int D;
int N;
long double TT;

void solvecase(){
	int k, cnt = 0;
	cin >> D >> N;
	TT = 0;
	//cerr << endl << S << endl;
	R.resize(N);
	for (auto it = R.begin(), _it = R.end(); it < _it; ++it)
	{
		unsigned long int t;
		cin >> t; get<0>(*it) = t;
		cin >> t; get<1>(*it) = t;
		//cerr << get<0>(*it) << " " << get<1>(*it) << endl;
	}
	sort (R.begin(),R.end());
	auto lh = R.end()-1;
	TT = ((long double)(D - get<0>(*lh) ))/(long double)(get<1>(*lh));
	for (auto it = R.end()-2, _it = R.begin(); it >= _it; --it)
	{
		if ( get<1>(*it) < get<1>(*lh) )
		{
			lh = it;
			TT = ((long double)(D - get<0>(*lh) ))/(long double)(get<1>(*lh));
		}
		else
		{
			long double tt = ((long double)(D - get<0>(*it) ))/(long double)(get<1>(*it));
			if (tt > TT)
			{
				TT = tt;
				lh = it;
			}
		}
		//cerr << get<0>(*it) << " " << get<1>(*it) << endl;
	}

	//cerr << "lst " << lstcs << endl;

	DONElbl:
	//for (auto it = R.begin(), _it = R.end(); it < _it; ++it) cin >> *it;
	cout <<std::fixed << std::setprecision(6) << ((long double)D)/TT;
}


int main(int argc, char** argv)
{
	// initialize static vars

	// test case processing
	unsigned int tstlmt;
	cin >> tstlmt;
	for (unsigned int tstcs = 1; tstcs <= tstlmt; ++tstcs)
	{
		cout << "Case #" << tstcs << ": " ;
		solvecase();
		cout << endl;
	}
	return 0;
}
