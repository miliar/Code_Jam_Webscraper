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

int main() {
	int t;
	cin >> t;
	for (int _ = 1; _ <= t; _++) {
		printf("Case #%d: ", _);
		int n, k;
		string s;
		cin >> s >> k;
		int cnt = 0;
		fo(i,0,sz(s)-k+1) {
			if (s[i] == '-') {
				fo(j,0,k) {
					s[i+j] = s[i+j] == '-'?'+':'-';
				}
				cnt++;
			}
		}
		fo(i,0,sz(s)) {
			if (s[i] == '-') {
				puts("IMPOSSIBLE"); goto here;
			}
		}
		printf("%d\n", cnt);
here:;
	}
	
	return 0;
}
