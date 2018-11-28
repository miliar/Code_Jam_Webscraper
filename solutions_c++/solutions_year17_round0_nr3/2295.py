#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <map>
 
using namespace std;

int test;
long long n, m;
map<long long, long long> C;

long long work(long long n, long long m) {
	if (m == 1)
		return n; 
	--m;
	if (m <= n / 2)
		return work(n / 2, m);
	else
		return work((n - 1) / 2, m - n / 2);
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("c.out", "w", stdout);
	scanf("%d", &test);
	for (int uu = 1; uu <= test; uu++)
	{
		scanf("%lld%lld", &n, &m);
		C.clear();
		C[n] = 1;
		for (;;) {
			map<long long, long long>::iterator itr = C.end();
			--itr;
			//cerr << itr->first << endl; 
			if (m <= itr->second)
			{
				printf("Case #%d: %lld %lld\n", uu, itr->first / 2, (itr->first - 1) / 2);
				break;
			}
			m -= itr->second;
			C[itr->first / 2] += itr->second;
			C[(itr->first - 1)/ 2] += itr->second;
			C.erase(itr);
		}		
	}
}
 
