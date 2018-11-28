#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <numeric>
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

string N;

void readCase()
{
	cin >> N;
}

void solve()
{
	string res = N;

	for(int i = 0; i < N.size() - 1; i++) {
		if(N[i] > N[i+1]) {
			int p = N[i+1];
			for(; i >= 0; i--) {
				if(p < N[i]) {
					res[i]--;
					for(int j = i + 1; j < res.size(); j++) {
						res[j] = '9';
					}
				}
				p = res[i];
			}			
			break;
		}
	}

	size_t ns = res.find_first_not_of("0");
	if( string::npos != ns )
	{
		res = res.substr( ns );
	}
	cout << res;
}

int main()
{
	//string fname = "./test/B-example.in";
	//string fname = "./test/B-small-attempt0.in";
	//string fname = "./test/B-small-attempt1.in";
	//string fname = "./test/B-small-attempt2.in";
	//string fname = "./test/B-small-practice.in";
	//string fname = "./test/B-large-practice.in";
	string fname = "./test/B-large.in";
	
	freopen(fname.c_str(),"r",stdin);freopen((fname+".out").c_str(),"w",stdout);

	cout << std::setprecision(10);

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

