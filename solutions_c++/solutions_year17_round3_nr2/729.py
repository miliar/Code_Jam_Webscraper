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

inline void assert(bool v)
{
	if(!v) 
		throw "ERROR";
}

#define memzero(V) memset( (V), 0, sizeof(V) )
inline void amin(int& A, int B) {
	if(A < B) return;
	A = B;
}
inline void amax(int& A, int B) {
	if(A > B) return;
	A = B;
}

int C;
int J;
bool AC[2 * 750];
bool AJ[2 * 750];

void readCase()
{
	cin >> C >> J;
	memzero(AC);
	memzero(AJ);
	for(int i = 0; i < C; i++) {
		int C, D;
		cin >> C >> D;
		for(int t = C; t < D; t++) AC[t] = true;
	}
	for(int i = 0; i < J; i++) {
		int C, D;
		cin >> C >> D;
		for(int t = C; t < D; t++) AJ[t] = true;
	}
}

void solve()
{
	static bool valid[2 * 750][2][750][750];
	typedef int stype[2][750][750];
	
	static stype sbuf[2];

	int best = INT_MAX;

	int cur = 0;

	for(int first = 0; first < 2; first++) {
		memzero(valid);
		memset(sbuf, 0x7f7f7f7f, sizeof(sbuf));

		valid[0][first][0][0] = true;
		valid[0][first ^ 1][0][0] = true;

		sbuf[cur][first][0][0] = 0;
		sbuf[cur][first ^ 1][0][0] = 1;
		
		for(int t = 0; t < 2 * 720 + 1; t++) {
			stype& switches = sbuf[cur];
			stype& next = sbuf[cur ^ 1];
			//memset(next, 0x7f7f7f7f, sizeof(next));
			for(int p = 0; p < 2; p++) {
				for(int c = 0; c < 721; c++) {
					int j = (t + 1) - c;
					next[p][c][j] = INT_MAX;
				}
			}
			for(int p = 0; p < 2; p++) {
				for(int c = 0; c < 721; c++) {
					//for(int j = t - c; j < 721; j++) {
						int j = t - c;
						if(t == 720 * 2)
							t = t;
						if(!valid[t][p][c][j]) continue;
						if(t == 2 * 720 && p == 1)
							t = t;
						assert(c + j == t);
						if(p == 0 && !AC[t]) {
							amin( next[0][c+1][j], switches[0][c][j] );
							valid[t+1][0][c+1][j] = true;
						}
						if(p == 1 && !AC[t]) {
							amin( next[0][c+1][j], switches[1][c][j] + 1 );
							valid[t+1][0][c+1][j] = true;
						}
						if(p == 1 && !AJ[t]) {
							amin( next[1][c][j+1], switches[1][c][j] );
							valid[t+1][1][c][j+1] = true;
						}
						if(p == 0 && !AJ[t]) {
							amin( next[1][c][j+1], switches[0][c][j] + 1 );
							valid[t+1][1][c][j+1] = true;
						}
					//}
				}
			}
			//memcpy(switches, next, sizeof(switches));
			cur = cur ^ 1;
		}
		if( first == 0 && valid[2 * 720 + 1][first][721][720] )
			amin(best, sbuf[cur][first][721][720] );
		if( first == 1 && valid[2 * 720 + 1][first][720][721] )
			amin(best, sbuf[cur][first][720][721] );
	}

	assert(best < INT_MAX);

	cout << best;
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

