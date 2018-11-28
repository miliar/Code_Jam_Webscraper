// ProblemA_AlphabetCake.cpp

#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <math.h>
#include <functional>
#include <sstream>
#include <cstring>
#include <set>
#include <map>
#include <cstdio>
#include <algorithm>
#include <bitset> 	
#include <ctime> 
#include <chrono>
#include <thread> 	
using namespace std;

// Shortcuts for "common" data types in contests

#define rep(i, a, b) for(int i = a; i < b; i++)
#define S(x) scanf("%d", &x)
#define S2(x, y) scanf("%d%d", &x, &y)
#define P(x) printf("%d\n", x)
#define all(v) v.begin(), v.end()
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

double computeDistance(int k, int d){

	double auxK = (double) k;
	double auxD = (double) d;

	return (d - k);
}

double getAns(int d, int n, int totInitPos[], int totMaxSpeed[]){

	double ans = 0.0;
	double longestTime = 0.0;

	forn(i, n)
		longestTime = max(longestTime, computeDistance(totInitPos[i], d)/totMaxSpeed[i]);

	return ((double) d)/longestTime;
}

int main(){

	int tc, d, n;
	S(tc);

	forn(i, tc){

		S2(d, n);
		int totInitPos[n];
		int totMaxSpeed[n];

		forn(j, n)
			S2(totInitPos[j], totMaxSpeed[j]);

		printf("Case #%d: %.10lf\n", i + 1, getAns(d, n, totInitPos, totMaxSpeed));
	}

	return 0;
}
