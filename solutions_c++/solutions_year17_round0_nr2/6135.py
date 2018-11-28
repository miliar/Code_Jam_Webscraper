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
		char s[20];
		scanf("%s", s);
		int len = strlen(s);
		if (len == 1) {
			printf("Case #%d: %s\n", nm, s);
			continue;
		}
		int pt0 = 0, pt1 = 0;
		for (int i=1;i<len;i++) {
			if (s[i] > s[i-1]) pt0 = i;
			if (s[i] >= s[i-1]) pt1 = i;
			if (s[i] < s[i-1]) break;
		}
		if (pt1 != len-1) {
			s[pt0]--;
			for (int i=pt0+1;i<len;i++) s[i] = '9';
		}
		if (s[0] == '0') printf("Case #%d: %s\n", nm, &s[1]);
		else printf("Case #%d: %s\n", nm, s);
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
