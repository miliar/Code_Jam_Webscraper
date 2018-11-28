#include <bits/stdc++.h>

#define maxn 100000008
#define pp push_back
#define pf push_front
#define mp make_pair
#define fs first
#define sc second

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int main(int argc, char *argv[])
{
	/* freopen("asmall.in", "r", stdin); */
	/* freopen("asmall.out", "w", stdout); */
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc) {
		string s;
		cin >> s;
		int k;
		scanf("%d", &k);
		int len = s.length();
		bool ok = true;
		int ans = 0;
		for (int i = 0; i < len; ++i) {
			if(s[i] == '+') continue;

			if(i+k > len){
				ok = false;
				break;
			} 

			for (int j = 0; j < k; ++j) {
				s[i+j] = (s[i+j] == '-' ? '+' : '-');
			}
			ans++;
		}
		printf("Case #%d: ", tc);
		if(ok) printf("%d\n", ans);
		else puts("IMPOSSIBLE");

		fprintf(stderr, "test %d solved -> %d\n", tc, ans);
	}
	return 0;
}
