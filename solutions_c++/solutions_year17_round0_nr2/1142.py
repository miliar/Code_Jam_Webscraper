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
#define F(x,y) for(typeof((y).begin()) x = (y).begin(); x != (y).end(); ++x) 
#define CHECKREAD(x, ...) if(scanf(__VA_ARGS__) != x) { fprintf(stderr, "Failed to read on %s, %d\n", __FILE__, __LINE__); exit(1); }


const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

bool solve(int P) {
	printf("Case #%d: ", P+1);
	string N;
	cin >> N;
	for(int i = 0; i < N.size() - 1; ++i) {
		if(N[i+1] < N[i]) {
			for(int j = i; j >= 0 && N[j+1] < N[j]; --j) {
				N[j+1] = '9';
				N[j] -= 1;
			}
			for(int j = i+1; j < N.size(); ++j) {
				N[j] = '9';
			}
			if(N[0] == '0') {
				N = N.substr(1);
			}
		}
	}
	cout << N << endl;
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
