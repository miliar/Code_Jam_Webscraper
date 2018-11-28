#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
using namespace std;
typedef long long ll;

int n, m, c;
struct A{
	int p, b;
} a[1000];
bool cmp(const A &a, const A &b) {
	if(a.b == b.b) return a.p < b.p;
	return a.b < b.b;
}
#define SWAP(X, Y) ((X)^=(Y)^=(X)^=(Y))

void T(int TC) {
	scanf("%d %d %d", &n, &c, &m);
	int i, j, k;
	for(i=0;i<m;i++) {
		scanf("%d %d", &a[i].p, &a[i].b);
	}

	int idx[1000];
	sort(a, a + m, cmp);
	for(i=0;i<n;i++) idx[i] = -1;
	for(i=0;i<m;i++) {
		if(idx[a[i].p] < 0)  idx[a[i].p] = i;
	}

	int min_r = (m - 1) / c + 1;
	int max_r = 1000;
	int y = 0, z = 0;

	int v[1001][1001] = {0};
	int sw[1000][2] = {0};
	int l = 0;
	for(i=0;i<m;i++) {
		if(a[i].b == 1) {
			v[l][1] = -1;
			v[l++][0] = i;
		} else {
			int same = -1, diff = -1;
			for(j=0;j<l;j++) {
				if(v[j][1] == -1) {
					if(same<0 && a[v[j][0]].p == a[i].p) same = j;
					if(diff<0 && a[v[j][0]].p != a[i].p) diff = j;
				}
			}
			if(diff >= 0) v[diff][1] = i;
			else if(same < 0 || a[i].p == 1) {
				if(same < 0) {
					for(j=0;j<l;j++) {
						if(a[v[j][0]].p != a[i].p
							 && a[v[j][0]].p == a[v[j][1]].p) {
							v[j][1] = i;
							break;
						}
					}
				}
				y++;
			} else {
				int t = -1;
				for(j=0;j<l;j++) {
					if(v[j][1] != -1 && a[v[j][1]].p != a[i].p) {
						t = j;
						if(a[v[j][0]].p == a[v[j][1]].p) break;
					}
				}
				if(t >= 0) {
					v[same][1] = v[t][1];
					v[t][1] = i;
				} else {
					v[same][1] = i;
				}
			}
		}
	}

	y += l;
	for(i=0;i<l;i++) {
		if(v[i][0] >= 0 && v[i][1] >= 0
			 && a[v[i][0]].p == a[v[i][1]].p) z++;
	}
	
	printf("%d %d\n", y, z);
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i=1;i<=t;i++) {
		printf("Case #%d: ", i);
		T(i);
	}
	return 0;
}
