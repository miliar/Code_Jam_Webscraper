#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <iostream>
using namespace std;

class node {
public:
	char c;
	int cnt;
	node () {
		c = cnt = 0;
	}
	node (char _c, int _cnt) {
		c = _c;
		cnt = _cnt;
	}
	bool operator < (const node &a) const {
		if (cnt != a.cnt) {
			return cnt > a.cnt;
		}
		return c < a.c;
	}
};

int main () {
	int t;
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	scanf ("%d", &t);

	for (int tc=1;tc<=t;tc++) {
		
		char c[] = "ROYGBV";
		node a[6];
		int n = 0;

		scanf ("%d", &n);
		for (int i=0;i<6;i++) {
			scanf ("%d", &a[i].cnt);
			a[i].c = c[i];
		}

		sort (a, a+6);

		if (a[0].cnt*2 > n) {
			printf ("Case #%d: IMPOSSIBLE\n", tc);
		}
		else {
			printf ("Case #%d: ", tc);
			int rem = max(a[1].cnt + a[2].cnt - a[0].cnt, 0);
			bool last = (a[1].cnt + a[2].cnt) >= a[0].cnt;
			for (int i=0;i<a[0].cnt;i++) {
				printf ("%c", a[0].c);
				if (i < a[0].cnt - 1 || last) {
					if (rem) {
						rem --;
						printf ("%c", a[2].c);
					}
					if (a[1].cnt) {
						printf ("%c", a[1].c);
						a[1].cnt --;
					} else {
						printf ("%c", a[2].c);
					}
				}
			}
			printf ("\n");
		}
	}

	return 0;
}