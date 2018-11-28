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
		cin >> s;
		bool flag;
		do {
			flag = false;
			rep(i, s.size()-1) {
				if(s[i] > s[i+1]) {
					--s[i];
					for(int j = i+1; j < s.size(); ++j) s[j] = '9';
					flag = true;
				}
			}
		} while(flag);
		printf("Case #%d: ", cas);
		if(s[0] == '0') {
			rep(i, s.size()-1) cout << '9';
		}
		else cout << s;
		puts("");
	}
	return 0;
}

