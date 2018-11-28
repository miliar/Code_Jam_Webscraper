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
using namespace std;

int D;
int N;
vector<int> K;
vector<int> S;

inline void assert(bool v)
{
	if(!v) 
		throw "ERROR";
}

void readCase()
{
	cin >> D >> N;
	K.clear();
	S.clear();
	for(int i = 0; i < N; i++) {
		int cK, cS;
		cin >> cK >> cS;
		K.push_back(cK);
		S.push_back(cS);
	}
}


void solve()
{
	double maxT = 0;
	for(int i = 0; i < N; i++) {
		double T = 1. * (D - K[i]) / S[i];
		maxT = max(maxT, T);
	}

	cout << D / maxT;
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

