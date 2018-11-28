#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <cstring>
using namespace std;

#define NN 1024
char s[NN];
int t;
int k;

const char x = '+' ^ '-';

int main()
{
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		scanf("%s%d", s, &k);
		int count = 0;
		int sl = strlen(s);
		for (int i = 0; i < sl - k + 1; ++i) {
			if (s[i] == '-') {
				for (int j = 0; j < k; ++j) {
					s[i+j] ^= x;
				}
				++count;
			}
		}
		for (int i = sl - k + 1; i < sl; ++i) {
			if (s[i] == '-') {
				count = -1;
				break;
			}
		}
		if (count == -1) {
			printf("Case #%d: IMPOSSIBLE\n", ti+1);
		} else {
			printf("Case #%d: %d\n", ti+1, count);
		}
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
