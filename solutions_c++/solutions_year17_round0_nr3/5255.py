// vudduu - codejam 2017 qualification round
// Problem C
#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_##i=(b);i<_##i;++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define MP          make_pair
#define S           size()
typedef long long   LL;

LL N, K;
map<LL, int> mapa;

void addNum(LL x, int y) {
    map<LL, int>::iterator it = mapa.find(x);
    if (it == mapa.end()) {
        mapa[x] = y;
    }
    else {
        mapa[x] = it->second + y;
    }
}

void solve() {
    cin >> N >> K;
    map<LL, int>::iterator it;
    mapa.clear();
    mapa[N] = 1;
    while (true) {
        it = mapa.end();
        it--;
        if (K <= it->second) break;
        LL div1 = it->first / 2LL;
        LL div2 = it->first - div1;
        addNum(div1, it->second);
        addNum(div2 - 1LL, it->second);
        K -= it->second;
        mapa.erase(it);
    }
    LL res1 = it->first / 2LL;
    LL res2 = it->first - res1 - 1LL;
    if (res2 < res1) swap(res1, res2);
    cout << res2 << " " << res1 << endl;
}

int main() {
    int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T ;cas++) {
        printf("Case #%d: ", cas);
        solve();
    }
}
