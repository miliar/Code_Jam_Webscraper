#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
 
#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
using namespace std;
 
#define fori(a,b) for(i = a; i <= b; i++)
#define forj(a,b) for(j = a; j <= b; j++)
#define fork(a,b) for(k = a; k <= b; k++)
#define scani(a) scanf("%d",&a);
#define scanlli(a) scanf("%lld", &a);
#define scanc(c) scanf("%c",&c);
#define scans(s) scanf("%s", s);
#define mp(a,b) make_pair(a, b)
#define ll(a) (long long int)(a)
#define vi vector<int>
#define vc vector<char>
#define vs vector<string>
#define println printf("\n");
#define sz(v) v.size()
#define len(s) s.length()
#define max(a,b) ((a > b) ? a : b)
#define min(a,b) ((a < b) ? a : b)

int main() {
	int t, k, i, j, l, len;
	char str[1003];
	scani(t)
	fori(1, t) {
		scanf("%s", str);
		scani(k)
		len = strlen(str);
		bool impossible = false;
		int cnt = 0;
		forj(0, len-1) {
			if (str[j] == '+') {
				continue;
			}
			for (int l = 0; l < k; l++) {
				if (l + j >= len) {
					impossible = true; 
					break;
				}
				if (str[l+j] == '-') {
					str[l+j] = '+';
				} else {
					str[l+j] = '-';
				}
			}
			cnt++;
			if (impossible) {
				break;
			}
		}
		if (impossible) {
			printf("Case #%d: IMPOSSIBLE\n", i);
		} else {
			printf("Case #%d: %d\n", i, cnt);
		}
	}
	return 0;
}