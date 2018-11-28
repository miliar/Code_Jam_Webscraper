#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <set>
#include <map>

using namespace std;

typedef long long lld;

int tt;
lld k, n;
map<lld, lld> M;

int main() {
	FILE *fout, *fin;
	fout = fopen("C.out", "wb");
	fin = fopen("C-large.in", "r");
	fscanf(fin, "%d", &tt);
	for (int t = 1 ; t <= tt ; t ++) {
		M.clear();
		fscanf(fin, "%lld %lld", &n, &k);
		M[n] = 1;
		k --;
		fprintf(fout, "Case #%d: ", t);
		while (k >= 0) {
			map<lld, lld>::iterator it = M.end();
			it --;
			if ((it->second) > k) break;
			else {
				lld a = (it->first), b = (it->second);
				M.erase(a);
				k -= b;
				M[a / 2] += b;
				M[(a - 1) / 2] += b;
			}
		}
		map<lld, lld>::iterator it = M.end();
		it --;
		fprintf(fout, "%lld %lld\n", (it->first) / 2, (it->first - 1) / 2);
	}
	fclose(fout);
	return 0;
}