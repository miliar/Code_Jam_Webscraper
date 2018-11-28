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

#define PROB_ID "B"
#define INPUT_SIZE  "small" // "large" //

typedef long double LD;
typedef unsigned long long ull;
int main()
{
	//freopen("my_input.txt", "r", stdin);
	//freopen("my_output.txt", "w", stdout);

	//freopen(PROB_ID "-" INPUT_SIZE "-attempt0.in", "r", stdin);
	//freopen(PROB_ID "-" INPUT_SIZE "-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	scanf("%d\n", &T); // remember to put \n

	rep(i, T) {
		// inputs
		char n[64];
		scanf("%s\n", n); // remember to put \n

		int len = strlen(n);
		if (len > 1) {
			bool check = true;
			while (check) {
				check = false;
				int idx = -1;
				for (int j = 0; j < len - 1; ++j) {
					if (n[j] > n[j + 1]) { check = true; idx = j; break; }
				}
				if (idx >= 0) {
					n[idx] = n[idx] - 1;
					for (int j = idx + 1; j < len; ++j) n[j] = '9';
				}
			}
			char* c = n;
			if (n[0] == '0') c = n+1;
			printf("Case #%d: %s\n", i + 1, c);

		} else {
			printf("Case #%d: %s\n", i + 1, n);
		}
	}
	return 0;
}

