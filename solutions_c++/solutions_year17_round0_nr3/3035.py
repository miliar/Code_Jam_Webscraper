#include <stdio.h>
#include <stack>
#include <map>
#include <string.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <math.h>
#include <vector>
#include <set>
#include <queue>
#include <fstream>
#include <functional>
using namespace std;
#define ll unsigned long long
#define mp make_pair
#define pb push_back
//#define ld long double
const double sn = 1e-6;
int t;
map <ll, ll> ma;
int main() {
	freopen("C-large.in","r",stdin);
	freopen("clarge.out", "w", stdout);
	scanf("%d", &t);
	for (int q = 1; q <= t; q++) {
		ll n, k;
		scanf("%I64d%I64d", &n, &k);
		ma[n] = 1;
		std::map<ll, ll>::reverse_iterator it = ma.rbegin();
		pair<ll, ll> res = mp(0,0);
		long long temp = k;
		while (it != ma.rend() && temp>0) {
			ll sp = (it->first)-1, tot = it->second;
			if (sp % 2 == 0) {
				res = mp(sp/2, sp/2);
				ma[sp / 2] += (2*tot);
			}
			else {
				res = mp(sp / 2+1, sp / 2);
				ma[sp / 2] += tot;
				ma[sp / 2 + 1] += tot;
			}
			temp -= tot;
			it++;
		}
		printf("Case #%d: %I64d %I64d\n", q, res.first, res.second);
		ma.clear();
	}
	return 0;
}