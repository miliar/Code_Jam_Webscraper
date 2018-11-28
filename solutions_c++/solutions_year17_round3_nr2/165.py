#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <iostream>

using namespace std;
#define dprintf debug && printf
#define doubt debug && cout
#define F(x,y) for(typeof((y).begin()) x = (y).begin(); x != (y).end(); ++x) 
#define CHECKREAD(x, ...) if(scanf(__VA_ARGS__) != x) { fprintf(stderr, "Failed to read on %s, %d\n", __FILE__, __LINE__); exit(1); }


const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

int best[1450][730][2][2];

bool solve(int P) {
	printf("Case #%d: ", P+1);
	vector<int> reqs(1440, -1);
	int ac, aj;
	cin >> ac >> aj;

	for(int i = 0; i < ac; ++i) {
		int f, t;
		cin >> f >> t;
		for(int k = f; k < t; ++k) {
			reqs[k] = 0;
		}
	}

	for(int i = 0; i < aj; ++i) {
		int f, t;
		cin >> f >> t;
		for(int k = f; k < t; ++k) {
			reqs[k] = 1;
		}
	}

	memset(best, 0x7f, sizeof(int) * 1450 * 730 * 2 * 2);
	best[0][0][0][0] = 0;
	best[0][0][1][1] = 0;
	best[0][0][1][0] = 1;
	best[0][0][0][1] = 1;

	for(int t = 1; t <= 1440; ++t) {
		for(int k = 0; k <= min(720, t); ++k) {
			if((reqs[t-1] == 0 || reqs[t-1] == -1) && k > 0) {
				best[t][k][0][0] = min(best[t-1][k-1][0][0], best[t-1][k-1][1][0] + 1);
				best[t][k][0][1] = min(best[t-1][k-1][0][1], best[t-1][k-1][1][1] + 1);
				doubt << "A: " << t << " " << k << " " << best[t][k][0][0] << " " << best[t][k][0][1] << endl;
			}
			if(reqs[t-1] == 1 || reqs[t-1] == -1) {
				best[t][k][1][0] = min(best[t-1][k][1][0], best[t-1][k][0][0] + 1);
				best[t][k][1][1] = min(best[t-1][k][1][1], best[t-1][k][0][1] + 1);
				doubt << "B: " << t << " " << k << " " << best[t][k][1][0] << " " << best[t][k][1][1] << endl;
			}
		}
	}

	int ret = min(best[1440][720][0][0], best[1440][720][1][1]);
	cout << ret << endl;
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
