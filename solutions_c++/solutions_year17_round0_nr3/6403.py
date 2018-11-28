#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <map>
#define P(a, b) make_pair(a, b)

using namespace std;

typedef long long ll;

const long long M = 1000000000000000000;

int main()
{
	FILE *infile, *outfile;
	infile = fopen("input.in", "r");
	outfile = fopen("output.txt", "w");
	int test_case;
	fscanf(infile, "%d", &test_case);

	for (int tc = 1; tc <= test_case; tc++) {
		map<pair<ll, ll>, ll> m;
		ll n, k;
		fscanf(infile, "%lld %lld", &n, &k);
		if (n % 2 == 0) {
			m.insert(P(P(M - (n / 2 - 1), M - (n / 2)), 1));
		}
		else {
			m.insert(P(P(M - (n / 2), M - (n / 2)), 1));
		}
		for (int i = 1; i < k; i++) {
			ll cmin, cmax, cnum;
			cmin = m.begin()->first.first;
			cmax = m.begin()->first.second;
			if ((--m[P(cmin, cmax)]) == 0) m.erase(P(cmin, cmax));
			cmin = M - cmin;
			cmax = M - cmax;
			if (cmax % 2 == 0 && cmax != 0) {
				ll nmin = M - (cmax / 2 - 1);
				ll nmax = M - (cmax / 2);
				if (m.find(P(nmin, nmax)) == m.end()) {
					m.insert(P(P(nmin, nmax), 1));
				}
				else {
					m[P(nmin, nmax)]++;
				}
			}
			else {
				ll nm = M - (cmax / 2);
				if (m.find(P(nm, nm)) == m.end()) {
					m.insert(P(P(nm, nm), 1));
				}
				else {
					m[P(nm, nm)]++;
				}
			}
			if (cmin % 2 == 0 && cmin != 0) {
				ll nmin = M - (cmin / 2 - 1);
				ll nmax = M - (cmin / 2);
				if (m.find(P(nmin, nmax)) == m.end()) {
					m.insert(P(P(nmin, nmax), 1));
				}
				else {
					m[P(nmin, nmax)]++;
				}
			}
			else {
				ll nm = M - (cmin / 2);
				if (m.find(P(nm, nm)) == m.end()) {
					m.insert(P(P(nm, nm), 1));
				}
				else {
					m[P(nm, nm)]++;
				}
			}

		}
		
		fprintf(outfile, "Case #%d: %lld %lld\n", tc, M - m.begin()->first.second, M - m.begin()->first.first);
	}

	fclose(infile);
	fclose(outfile);

	return 0;
}