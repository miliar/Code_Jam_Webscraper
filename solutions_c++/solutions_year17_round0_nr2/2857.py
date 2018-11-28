#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	int tc;
	unsigned long long N, M;
	freopen("inp.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &tc);
	for (int t = 0; t < tc; ++t) {
		scanf("%I64u", &N);
		printf("Case #%d: ", t + 1);
		M = N;
		vector <int> st(19, 0), buf (19, 0);
		int i = 0;
		while (N) {
			st[i] = N % 10;
			N /= 10;
			++i;
		}
		int flag = 0;
		int p = 0;
		while (!flag) {
			int j = 0;
			for (j = p; j < 18; ++j) {
				if (st[j] < st[j + 1]) {
					break;
				}
			}
			p = j;
			if (j == 18) {
				flag = 1;
			} else {
				for (int k = 0; k <= j; ++k)
					st[k] = 9;
				++j;
				for (;j < 19; ++j) {
					if (st[j] > 0) {
						--st[j];
						break;
					} else {
						st[j] = 9;
					}
				}
			}
		}
		for (int i = 18; i >= 0; --i) {
			N*= 10;
			N += st[i];
		}
		printf("%I64u\n", N);
	}
	return 0;
}