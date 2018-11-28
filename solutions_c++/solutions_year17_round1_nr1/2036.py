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
#define INPUT_SIZE  "small" //"large" // 

typedef long double LD;


int main()
{
	//freopen("my_input.txt", "r", stdin);
	//freopen("my_output.txt", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	//freopen(PROB_ID "-" INPUT_SIZE "-attempt0.in", "r", stdin);
	//freopen(PROB_ID "-" INPUT_SIZE "-attempt0.out", "w", stdout);

	int T;
	scanf("%d\n", &T); // remember to put \n

	rep(i, T) {
		// inputs
		int R, C;
		scanf("%d %d\n", &R, &C); // remember to put \n
		vector<string> v;
		rep(r, R) { // read each row
			char s[64];
			scanf("%s\n", s);
			v.push_back(string(s));
		}

		// fill character for each row
		rep(r, R) {
			rep(c, C) {
				int k = -1;
				if (v[r][c] != '?') {
					for (k = 0; k < c; ++k) {
						if (v[r][k] == '?') v[r][k] = v[r][c];
					}
				}
				if ((k != -1) && (k < C)) {
					for (; k < C; ++k) if (v[r][k] == '?') v[r][k] = v[r][k - 1];
				}
			}
		}

		rep(c, C) {
			rep(r, R) {
				int k = -1;
				if (v[r][c] != '?') {
					for (k = 0; k < r; ++k) {
						if (v[k][c] == '?') v[k][c] = v[r][c];
					}
				}
				if ((k != -1) && (k < R)) {
					for (; k < R; ++k) if (v[k][c] == '?') v[k][c] = v[k - 1][c];
				}
			}
		}
		
		printf("Case #%d:\n", i + 1);
		rep(r, R) {
			rep(c, C) {
				printf("%c", v[r][c]);
			}
			printf("\n");
		}
	}
	return 0;
}

