// Lupus Nocawy
// 2017-04-22
// Google Code Jam
// Round 1B 2017
// https://code.google.com/codejam
// https://code.google.com/codejam/contest/8294486/dashboard
// Problem A

#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <cmath>
using namespace std;
#define REP(i,n) for(int i=0, _n=n; i<_n; ++i)
#define FOR(i,a,b) for(int i=(a), _b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a), _b=(b); i>=_b; --i)
#define IT(i,x) __typeof__(x) i=x
#define FOREACH(it,x) for(__typeof__((x).begin()) it=(x).begin(); it!=(x).end(); ++it)
#define ALL(x) x.begin(),x.end()
#define MP make_pair
#define PB push_back
#define DEBUG(x) if(debug) cout << x << endl;
typedef long long int lli;
typedef unsigned long long int llu;
typedef pair<int,int> pii;
const int debug=0;

const int INF = 2147483647;
const int max_n = 2147483647;

void solve(int c){
	int D, N;
	scanf("%d %d ", &D, &N);
	double Tmax = 0;
	REP(i,N){
		int K, S;
		scanf("%d %d ", &K, &S);
		double T = (double)(D-K) / (double)S;
		Tmax = max(Tmax,T);
	}

	double V = (double)D / Tmax;
	printf("%lf\n", V);

	return;
}

int main(void){
	int t;
	scanf("%d ", &t);
	for(int c=1; c<=t; ++c){
		printf("Case #%d: ", c);
		solve(c);
	}
	return 0;
}
