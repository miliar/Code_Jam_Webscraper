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
using namespace std;
#define ll long long
#define mp make_pair
#define pb push_back
//#define ld long double
const double sn = 1e-6;
int t;
int main() {
	freopen("B-large.in","r",stdin);
	freopen("blarge.out", "w", stdout);
	scanf("%d", &t);
	for (int q = 1; q <= t; q++) {
		ll n;
		scanf("%I64d", &n);
		string s = to_string(n);
		int sz = s.size();
		for (int i = sz - 1; i >= 0; i--) {
			if (i != sz - 1 && s[i] > s[i + 1]) {
				s[i]--;
				for (int j = i + 1; j < sz; j++) {
					s[j] = '9';
				}
			}
		}
		printf("Case #%d: ", q);
		bool v = true;
		for (int i = 0; i < sz; i++) {
			if (v&&s[i] == '0')
				continue;
			else {
				v = false;
				printf("%c", s[i]);
			}
		}
		printf("\n");
	}
	return 0;
}