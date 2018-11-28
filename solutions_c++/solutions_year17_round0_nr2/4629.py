/*	In the name of God	*/
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

using namespace std;

char s[101];
int main() {
	int tc, k;
	ll n;
	freopen("B-large.in", "r", stdin);
	freopen("program.out", "w", stdout);
	cin >> tc;
	for (int ti = 0; ti < tc; ++ti) {
		cin >> n;
		sprintf(s, "%lld", n);
		int i;
		for (i = 1; s[i]; ++i) {
			if (s[i] < s[i - 1])
				break;
		}
		printf("Case #%d: ", ti + 1);
		if (!s[i]) {
			printf("%s\n", s);
			continue;
		}
		for (i = 0; s[i] == '1'; ++i);
		
//		for (; s[i] == '0'; ++i);
		if (s[i]=='0') {
			s[strlen(s) - 1] = 0;
			for (int i = 0; s[i]; ++i) {
				s[i] = '9';
			}
			printf("%s\n", s);
			continue;
		}
		while (1) {
//			char tmp[31];
//			memset(tmp, '0', 21);
//			tmp[21] = 0;
			for (i = 1; s[i]; ++i) {
				if (s[i] < s[i - 1])
					break;
			}
			if (!s[i]) {
				printf("%s\n", s);
				break;
			}
			i--;
//			if (s[i] == '0') {
//				ll x = 1;
//				for (int j = 0; j < strlen(s) - i; ++j) {
//					x *= 10;
//				}
//				n -= x;
//				sprintf(s, "%lld", n);
//			} else {
			s[i]--;
			for (int j = i + 1; s[j]; ++j) {
				s[j] = '9';
			}
			
		}
	}
	
	
	return 0;
}