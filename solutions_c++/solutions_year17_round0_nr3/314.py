#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <sstream>
#include <algorithm>
using namespace std;

typedef long long ll;

int t;
ll n, k;

int main()
{
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		cin >> n >> k;
		map <ll, ll> M; M[n]++;
		for (map <ll, ll>::reverse_iterator it = M.rbegin(); it != M.rend() && k > 1; it++) {
			ll tk = min(it->second, k - 1);
			it->second -= tk; k -= tk;
			M[it->first / 2] += tk; 
			M[(it->first - 1) / 2] += tk;
		}
		map <ll, ll>::reverse_iterator pnt = M.rbegin();
		while (pnt->second == 0) pnt++;
		printf("Case #%d: %lld %lld\n", tc, pnt->first / 2, (pnt->first - 1) / 2);
	}
	return 0;
}