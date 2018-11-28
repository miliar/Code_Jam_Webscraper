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
#include <list>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
#include <iomanip>
using namespace std;

long long N;
long long K;

inline void assert(bool v)
{
	if(!v) 
		throw "ERROR";
}

void readCase()
{
	cin >> N >> K;
}

void solve()
{
	map< long long, long long, greater<long long> > set;

	set[N] = 1LL;

	while(K > 0) {
		long long sz = set.begin()->first;
		long long cnt = min( set.begin()->second, K );
		set[sz] -= cnt;
		if( set[sz] == 0 ) {
			set.erase( sz );
		}
		long long m = (sz - 1) / 2;
		long long M = sz / 2;
		set[ m ] += cnt;
		set[ M ] += cnt;
		
		K -= cnt;
		if(K == 0) {
			cout << M << " " << m;
			return;
		}
	}
}

int main()
{
	//string fname = "./test/C-example.in";
	//string fname = "./test/C-small-1-attempt0.in";
	//string fname = "./test/C-small-2-attempt0.in";
	string fname = "./test/C-large.in";

	freopen(fname.c_str(),"r",stdin);freopen((fname+".out").c_str(),"w",stdout);

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

