#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <unordered_map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue> 
#include <cctype> 
#include <cassert>

using namespace std;

#define VV vector
#define PB push_back
#define SZ(v) ((int)(v).size()) 
#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(decltype((b).begin()) a = (b).begin();a!=(b).end();++a)
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi VV<int>
#define vs VV<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))

#define PROB_ID "C"
#define INPUT_SIZE  "small-2" //"large" // 

typedef long double LD;
typedef unsigned long long llu;

void output(int i, llu M, llu m) { printf("Case #%d: %llu %llu\n", i + 1, M, m); }

int main()
{
	//freopen("my_input.txt", "r", stdin);
	//freopen("my_output.txt", "w", stdout);

	//freopen(PROB_ID "-" INPUT_SIZE "-attempt0.in", "r", stdin);
	//freopen(PROB_ID "-" INPUT_SIZE "-attempt0new.out", "w", stdout);

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int T;
	scanf("%d\n", &T); // remember to put \n

	rep(i, T) {
		priority_queue<llu> heap;
		unordered_map<llu, llu> hm;
		// inputs
		llu N;
		llu K;
		scanf("%llu %llu\n", &N, &K); // remember to put \n
		//if (K > (N + 1 / 2)) { output(i, 0, 0); continue; }

		heap.push(N);
		hm[N] = 1;
		llu m = 0, M = 0;
		for (llu j = 0; j < K;) {
			llu val = heap.top(); 
			if (val == 1) { M = 0; m = 0; break; }

			M = val / 2;
			if (val % 2 == 0) m = M - 1; // even cases
			else m = M; // odd cases

			if (hm[val] + j >= K) break;
			heap.pop();
			j = j + hm[val];
			if (hm[M] == 0) heap.push(M);
			if ((M != m) && (hm[m] == 0)) heap.push(m);
			hm[M] += hm[val];
			hm[m] += hm[val];
			hm[val] = 0;
		}
		output(i, M, m);
	}
	return 0;
}

