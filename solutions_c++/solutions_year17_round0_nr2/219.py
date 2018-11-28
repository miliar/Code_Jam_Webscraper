#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <cstring>
using namespace std;

#define NN 32
int t;
char s[NN];

int main()
{
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		scanf("%s", s);
		int sl = strlen(s);
		for (int i = sl - 1; i > 0; --i) {
			if (s[i-1] > s[i]) {
				--s[i-1];
				for (int j = i; j < sl; ++j) {
					s[j] = '9';
				}
			}
		}
		for (int i = 0; i < sl; ++i) {
			if (s[i] != '0') {
				printf("Case #%d: %s\n", ti+1, s + i);
				break;
			}
		}
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
