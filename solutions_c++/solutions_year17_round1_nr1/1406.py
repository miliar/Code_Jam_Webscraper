#include <bits/stdc++.h>

#define maxn 200100
#define sq 333
#define logn 23
#define inf 0x3F3F3F3F
#define linf 0x3F3F3F3F3F3F3F3FLL
#define eps 1e-9
#define pb push_back
#define mp make_pair
#define mod 1000000007LL

using namespace std;

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;
typedef priority_queue<pii, vii, greater<pii> > pq;

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

char s[30][30];
int t, n, m;
int ck[300];

int main() {
	scanf("%d", &t);
	for(int cas = 1; cas <= t; ++cas) {
		memset(ck, 0, sizeof ck);
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; ++i) {
			scanf("%s", s[i]);
			for(int j = 0; j < m; ++j) {
				int jj = j-1;
				while(jj >= 0 && s[i][jj] == '?') {
					s[i][jj--] = s[i][j];
				}
				jj = j+1;
				while(jj < m && s[i][jj] == '?') {
					s[i][jj++] = s[i][j];
				}
			}
		}
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < m; ++j) {
				if(s[i][j] != '?' && !ck[s[i][j]]) {
					ck[s[i][j]] = 1;

					int x = j+1;
					while(x < m && s[i][x] == s[i][j]) x++;
					x--;

					int k = i-1;
					while(k >= 0) {
						int ok = 1;
						for(int y = j; y <= x; ++y) {
							if(s[k][y] != '?') {
								ok = 0;
								break;
							}
						}
						if(!ok) break;
						else {
							for(int y = j; y <= x; ++y) {
								s[k][y] = s[i][j];
							}
							k--;
						}
					}
					k = i+1;
					while(k >= 0) {
						int ok = 1;
						for(int y = j; y <= x; ++y) {
							if(s[k][y] != '?') {
								ok = 0;
								break;
							}
						}
						if(!ok) break;
						else {
							for(int y = j; y <= x; ++y) {
								s[k][y] = s[i][j];
							}
							k++;
						}
					}
				}				
			}
		}
		printf("Case #%d:\n", cas);
		for(int i = 0; i < n; ++i) {
			printf("%s\n", s[i]);
		}
	}

	return 0;
}