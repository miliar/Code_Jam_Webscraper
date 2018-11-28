#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
#include <iomanip>
#include <cmath>
using namespace std;

const double PI = atan(1.0)*4;

int N;
int K;
vector< pair<double, double> > RH;

inline void assert(bool v)
{
	if(!v) 
		throw "ERROR";
}

void readCase()
{
	cin >> N >> K;
	RH.clear();
	for(int i = 0; i < N; i++) {
		int cR, cH;
		cin >> cR >> cH;
		RH.push_back( make_pair(cR, cH) );
	}
}

double area(double R, double H, double R2)
{
	return 2 * PI * R * H + PI * R * R - PI * R2 * R2;
}

void solve()
{
	sort(RH.begin(), RH.end(), greater< pair<double, double> >() );

	double maxA = 0;

	static double marea[1000][1000];
	memset(marea, 0, sizeof(marea));

	for(int i = 0; i < N; i++) {
		double maxAK = 0;
		for(int remK = K; remK > 0; remK--) {
			maxAK = max(maxAK, marea[i][remK]);
			if(remK == 1) {
				double curA = maxAK + area( RH[i].first, RH[i].second, 0 );
				maxA = max(maxA, curA);
			} else 
				for(int j = i + 1; j < N; j++) {
					double curA = maxAK + area( RH[i].first, RH[i].second, RH[j].first );
					marea[j][remK - 1] = max( marea[j][remK - 1], curA );
				}
		}
	}

	cout << maxA;
}

int main()
{
	//string fname = "./test/A-example.in";
	//string fname = "./test/A-small-attempt0.in";
	//string fname = "./test/A-small-attempt1.in";
	string fname = "./test/A-large.in";
	
	freopen(fname.c_str(),"r",stdin);freopen((fname+".out").c_str(),"w",stdout);
	cout << std::setprecision(18);

	int analizeCase = -1;
	
	int T;
	scanf("%d", &T);
	for(int tCase = 1; tCase <= T; tCase++) {
		printf("Case #%d: ", tCase);
		readCase();
		if(analizeCase < 0 || analizeCase == tCase) solve();
		printf("\n");
		fflush(stdout);
		fprintf(stderr, "Done %d %%     \r", 100 * tCase / T );
	}
	return 0;
}

