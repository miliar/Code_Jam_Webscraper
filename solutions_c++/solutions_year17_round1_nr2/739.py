#include<bits/stdc++.h>
#define ms(x, y) memset(x, y, sizeof(x))
#define rep(i, a, b) for(int i = a; i <= b; i++)
#define ll long long 
using namespace std;


int a[60][60];
int de[60];
int po[60];
int n, p;

int L[60][60], R[60][60];


int main () {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int tc;
	cin >> tc;
	rep(tt, 1, tc) {
		cin >> n >> p;
		rep(i, 1, n)
			scanf("%d", &de[i]);
		rep(i, 1, n)
			po[i] = 0;

		int ma = 0;
		rep(i, 1, n) {
			rep(j, 1, p) {
				scanf("%d", &a[i][j]);
			}
			sort(1+a[i], 1+p+a[i]);
			rep(j, 1, p) {
				L[i][j] = ceil(1.0 * a[i][j] / 1.1 / de[i]);
				R[i][j] = floor(1.0 * a[i][j] / 0.9 / de[i]);
				ma = max(ma, R[i][j]);
			}
		}

		int tmp[60];
		int ans = 0;
		rep(kit, 0, ma) {
			while(true) {
				rep(i, 1, n) {
					bool flag = false;
					rep(j, po[i]+1, p) {
						if(L[i][j] <= kit && R[i][j] >= kit) {
							tmp[i] = j;
							flag = true;
							break;
						}
					}
					if(flag == false) {
						goto l1;
					}
				}
				ans++;
				rep(i, 1, n) {
					po[i] = tmp[i];
				}
			}
			l1: ;
		}

		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}