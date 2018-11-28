#include <bits/stdc++.h>

#define sz(z) (int)z.size()
#define fo(i,a,b) for (auto (i) = (a); (i) < (b); (i)++)
#define mp make_pair
#define pb push_back

using namespace std;

#define DEBUG

#ifdef DEBUG
#define D(x...) printf(x)
#else
#define D(x...) 
#endif

typedef long long ll;
typedef pair<int,int> ii;

int act[241*61];
int rec[241*61];

const int t = 24*60;

int main() {
	int T;
	scanf("%d\n", &T);
	for (int _ = 1; _ <= T; _++) {
		printf("Case #%d: ", _);
		int ac, aj;
		scanf("%d %d", &ac, &aj);
		fo(i,0,241*61) act[i] = 0;
		fo(i,0,t) rec[i] = 0;
		int st = 12345667;
		fo(i,0,ac) {
			int a, b;
			scanf("%d %d", &a, &b);
			fo(j,a,b) act[j] = 1, rec[j] = 2;
			st = min(st, a);
		}
		fo(i,0,aj) {
			int a, b;
			scanf("%d %d", &a, &b);
			fo(j,a,b) act[j] = 2, rec[j] = 1;
			st = min(st, a);
		}

		int ans = 4;
		int ar[123];
		int tmp[t];
		int kek[1555];
		fo(i,0,t) kek[i] = 0;
		fo(i,0,t) {
			fo(j,0,t/2) {
				kek[(i+j)%t] = 1;	
			}
			fo(j,t/2,t) {
				kek[(i+j)%t] = 2;	
			}
			bool good = 1;
			fo(j,0,t) {
				if (kek[j] == rec[j]) {
					good = 0;
				}
			}
			if (good) {
				printf("%d\n",2);
				goto kr;
			}
		}
		printf("4\n");
		goto kr;

		ar[0] = ar[1] = ar[2];
		fo(i,0,t) tmp[i] = rec[i], ar[rec[i]]++;;
		fo(i,0,24*60) {
			// starting at i
			if ((rec[i] && rec[(i+1)%t] == 0)) {
				fo(curr,1,3) {
					ar[0] = ar[1] = ar[2] = 0;
					fo(j,0,t) tmp[j] = rec[j];
					int cur = curr;
					fo(j,0,24*60) {
						int k = j + i;
						k %= t;
						if (tmp[k] == 0) {
							if (ar[cur] == 720) {
								cur = 3-cur;
							}
						} else {
							cur = tmp[k];
						}
						tmp[k] = cur;
						ar[cur]++;
						if (ar[cur] > 720) {
							goto here;
						}		
					}
				}
				int cr = 0;
				fo(j,0,t) {
					if (tmp[j] != tmp[(j+1)%t]) {
						cr++;
					}
				}
				ans = min(ans, cr);
			}
here:;
		}
		printf("%d\n", ans);
kr:;
	}
	
	return 0;
}
