#include <bits/stdc++.h>
using namespace std;
#define ULL unsigned long long
#define LL long long
#define rep(i,n) for(int i = 0; i < n; ++i)
#define Rep(i,n) for(int i = 1; i <= n; ++i)

const int INF = 0x3f3f3f3f;

int main()
{
	int t, cas = 0;
	cin >> t;
	while(cas++ < t) {
		string s;
		int n, ans = 0;
		cin >> s >> n;
		rep(i, s.size()-n+1) {
			if(s[i] == '-') {
				for(int j = i; j < i+n; ++j) s[j] ^= 6;
				++ans;
			}
		}
		for(int i = s.size()-n+1; i < s.size(); ++i) {
			if(s[i] == '-') ans = -1;
		}
		printf("Case #%d: ", cas);
		if(ans < 0) puts("IMPOSSIBLE");
		else cout << ans << '\n';
	}
	return 0;
}

