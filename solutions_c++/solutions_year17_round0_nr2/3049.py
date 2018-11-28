#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define ALL(c) (c).begin(),(c).end()

string s;
int TC;

int main() {
	scanf("%d", &TC);
	rep(tc, TC) {
		cin >> s;
		reverse(ALL(s));

		for (int i = 0; i+1 < s.size(); ++i) {
			if (s[i] < s[i+1]) {
				--s[i+1];
				for (int j = 0; j <= i; ++j) {
					s[j] = '9';
				}
			}
		}
		while (s.size() && s[s.size()-1] == '0') {
			s.pop_back();
		}
		reverse(ALL(s));

		printf("Case #%d: %s\n", tc + 1, s.c_str());

	}
	return 0;
}