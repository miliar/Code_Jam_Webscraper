#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
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
#define ll long long
#define ld long double
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

#define PROB_ID "A"
#define INPUT_SIZE  "large" //"small" // 

typedef long double LD;



int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	//freopen(PROB_ID "-" INPUT_SIZE "-attempt0.in", "r", stdin);
	//freopen(PROB_ID "-" INPUT_SIZE "-attempt0.out", "w", stdout);

	int T;
	scanf("%d\n", &T); // remember to put \n

	rep(i, T) {
		// inputs
		int k;
		char S[1024];
		scanf("%s %d\n", S, &k); // remember to put \n

		int rows = strlen(S);
		int flips = 0;
		int lastIdx = rows - k;
		for (int j = 0; j <= lastIdx; ++j) {
			while ((j <= lastIdx) && (S[j] == '+')) ++j;
			if (j > lastIdx) break;
			for (int f = j; f < j + k; ++f) {
				S[f] = (S[f] == '-') ? '+' : '-';
			}
			++flips;
		}
		// Check last K
		bool bDone = true;
		int x = max(lastIdx, 0);
		for (; x < rows; ++x) { if (S[x] == '-') { bDone = false; break; } }

		if (bDone) printf("Case #%d: %d\n", i + 1, flips);
		else printf("Case #%d: IMPOSSIBLE\n", i + 1);
	}
	return 0;
}

