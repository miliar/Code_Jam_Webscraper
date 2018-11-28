#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
#include <climits>
#include <set>
#include <cmath>
#define ll long long

using namespace std;

struct aa {
    int x, y;
    bool operator < (const aa &b) {
        if (x != b.x) return x < b.x;
        return y < b.y;
    }
};

bool cmp(int a, int b) {return a > b;}
int bsearch(int *a, int n, int k);

int main() {
	int T;
	cin >> T;
	for (int nm=1;nm<=T;nm++) {
		char s[1005];
		int k, ct = 0;
		scanf("%s%d", s, &k);
		int len = strlen(s);
		for (int i=0;i<len - k + 1;i++) {
			if (s[i] == '-') {
				for (int j=i;j<i+k;j++) {
					if (s[j] == '+') s[j] = '-';
					else s[j] = '+';
				}
				ct++;
			}
		}
		bool pass = true;
		for (int i=0;i<len;i++) if (s[i] == '-') pass = false;
		if (pass) printf("Case #%d: %d\n", nm, ct);
		else printf("Case #%d: IMPOSSIBLE\n", nm);
	}
	return 0;
}

int bsearch(int *a, int n, int k) {
    int l = 0, h = n;
    while (l < h) {
        int m = (l + h) / 2;
        if (a[m] == k) return m;
        else if (a[m] > k) h = m;
        else l = m + 1;
    }
    return l;
}
