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
#include <iomanip>

using namespace std;
#define dprintf debug && printf
#define doubt debug && cout
#define F(x,y) for(typeof((y).begin()) x = (y).begin(); x != (y).end(); ++x) 
#define CHECKREAD(x, ...) if(scanf(__VA_ARGS__) != x) { fprintf(stderr, "Failed to read on %s, %d\n", __FILE__, __LINE__); exit(1); }


const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

const long double eps = 1e-10;

void init() {
}

bool solve(int P) {
	printf("Case #%d: ", P+1);
	int N, K;
	cin >> N >> K;
	assert(N == K);
	vector<long double> probs(N);
	long double U;
	cin >> U;
	for(int i = 0; i < N; ++i) {
		cin >> probs[i];
	}

	sort(probs.begin(), probs.end());
	while(U > eps) {
		int i = 0;
		for(i = 0; i < N && abs(probs[0] - probs[i]) < eps; ++i);

		long double target = 1;
		if(i < N) {
			target = probs[i];
		}
		if(U >= i * (target - probs[0])) {
			U -= i * (target - probs[0]);
			for(int k = 0; k < i; ++k) {
				probs[k] = target;
			}
		} else {
			for(int k = 0; k < i; ++k) {
				probs[k] += U / i;
			}
			U = 0;
		}
	}

	long double p = 1;
	for(int i = 0; i < N; ++i) {
		doubt << probs[i] << endl;
		p *= probs[i];
	}
	cout << fixed << setprecision(9) << p << endl;
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
