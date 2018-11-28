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

typedef long long ll;


const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

bool solve(int P) {
	printf("Case #%d: ", P+1);
	map<ll, ll> segs;
	ll N, K;
	cin >> N >> K;
	segs[-N] = 1;
	while(K > 0) {
		const ll c = segs.begin()->second;
		const ll sz = -segs.begin()->first;
		assert(sz >0);
		dprintf("%lld %lld %lld\n", c, sz, K);
		if(c >= K) {
			cout << sz / 2 << ' ' << (sz - 1) / 2 << endl;
		} else {
			segs[-(sz/2)] += c;
			segs[-((sz-1)/2)] += c;
		}
		segs.erase(segs.begin());
		K -= c;
	}
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
