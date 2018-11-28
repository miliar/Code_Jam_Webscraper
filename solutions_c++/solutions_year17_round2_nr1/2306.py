#include "string" 
#include "iostream"
#include "sstream"
#include "vector"
#include "map"
#include "queue"
#include "algorithm"
#include "functional"
#include "set"
#include "tuple"
using namespace std;

#define LL long long
#define UL unsigned long long

#define VC vector<char>
#define VI vector<int>
#define VU vector<unsigned int>
#define VL vector<long long>
#define VUL vector<unsigned long long>
#define VS vector<string>
#define VD vector<double>
#define VB vector<bool>
#define VC_IT VC::iterator;
#define VI_IT VI::iterator
#define VU_IT VU::iterator
#define VL_IT VL::iterator
#define VUL_IT VUL::iterator
#define VS_IT VS::iterator
#define VD_IT VD::iterator
#define VB_IT VB::iterator;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (decltype(n) i = 0; i < (n); ++i)
#define FOR(var, start, end) for (decltype(start) var = (start); var <= (end); ++var)
#define FORD(var, start, end) for (decltype(start) var = (start); var >= (end); --var)
#define FOREACH(it, X) for( decltype((X).begin()) it = (X).begin(); it != (X).end(); ++it)

void doCase(int iCase) {
	printf("Case #%d: ", iCase);

	LL D, N;
	cin >> D >> N;

	double Tmax = 0.0;
	REP(i, N) {
		LL K, S;
		cin >> K >> S;
		double T = (double)(D - K) / (double)S;
		if (T > Tmax)
			Tmax = T;
	}

	printf("%.6f\n", D / Tmax);
}

void main(void) {
	int nCases;
	cin >> nCases;
	cin.ignore(999, '\n');

	for (int iCase = 1; iCase <= nCases; iCase++) {
		doCase(iCase);
	}
}