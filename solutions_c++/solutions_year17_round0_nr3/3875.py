#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

typedef long long LL;

using namespace std;

priority_queue<LL> heap;
map<LL, LL> mapa;

int main() {
  freopen("Cl.out","wt", stdout);
  freopen("Cl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests) {
    cout << "Case #" << (test + 1) << ": ";
    while (!heap.empty())
			heap.pop();
		mapa.clear();
		LL n, k;
		cin >> n >> k;
		mapa[n] = 1LL;
		heap.push(n);
		LL last = -1LL;
		while (k > 0) {
			LL el = heap.top();
			heap.pop();
			last = el;
			LL cnt = mapa[el];
			k -= cnt;
			mapa[el] = 0;
			LL val1 = (el + 1) / 2 - 1;
			LL val2 = el - val1 - 1;
			if (mapa[val1] == 0)
				heap.push(val1);
			if (mapa[val2] == 0)
				heap.push(val2);
			mapa[val1] += cnt;
			mapa[val2] += cnt;
		}
		LL val1 = (last + 1) / 2 - 1;
		LL val2 = last - val1 - 1;
		cout << val2 << " " << val1;
    cout << "\n";
  }
  return 0;
}
