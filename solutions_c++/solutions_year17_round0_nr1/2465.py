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
using namespace std;

int K;
string S;

inline void assert(bool v)
{
	if(!v) 
		throw "ERROR";
}

void readCase()
{
	cin >> S;
	cin >> K;
}


void solve()
{
	int cnt = 0;
	for(int i = 0; i < S.size() - K + 1; i++) {
		if(S[i] != '+') {
			for(int j = 0; j < K; j++) {
				S[i + j] = S[i + j] ^ '+' ^ '-';
			}
			cnt++;
		}
	}
	if(S.find('-') !=  string::npos) {
		cout << "IMPOSSIBLE";
		return;
	}
	cout << cnt;
}

int main()
{
	//string fname = "./test/A-example.in";
	//string fname = "./test/A-small-attempt0.in";
	string fname = "./test/A-large.in";
	
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

