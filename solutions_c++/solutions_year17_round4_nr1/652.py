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

int best[110][110][110][5];

int opt(int p, int c1, int c2, int c3, int cur) {
	int &ret = best[c1][c2][c3][cur];
	if(ret != -1)
		return ret;
	ret = 0;

	if(c1 || c2 || c3) {
		int base = 0;
		if(cur == 0)
			++base;
		if(c1) {
			ret = max(ret, base + opt(p, c1 - 1, c2, c3, (cur - 1 + p) % p));
		}
		if(c2) {
			ret = max(ret, base + opt(p, c1, c2 - 1, c3, (cur - 2 + p) % p));
		}
		if(c3) {
			ret = max(ret, base + opt(p, c1, c2, c3 - 1, (cur - 3 + p) % p));
		}
	}

	doubt << "opt" << p << " " << c1 << " " << c2 << " " << c3 << " " << cur << " = " << ret << endl;

	return ret;
}

bool solve(int P) {
	printf("Case #%d: ", P+1);
	int N, p;
	cin >> N >> p;
	assert(p <= 4);
	vector<int> count(4);
	memset(best, -1, sizeof(int) * 110 * 110 * 110 * 5);
	for(int i = 0; i < N; ++i) {
		int tmp;
		cin >> tmp;
		count[tmp % p]++;
	}
	doubt << count[0] << " " << count[1] << " " << count[2] << " " << count[3] << endl;

	cout << count[0] + opt(p, count[1], count[2], count[3], 0) << endl;
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
