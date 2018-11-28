#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T, kase = 0;
	scanf("%d",&T);
	while (T--) {
		ll x;
		scanf("%lld",&x);
		string s;
		while (x) {
			s += x % 10 + '0';
			x /= 10;
		}
		reverse(s.begin(),s.end());
		int len = s.size();
		for (int i = len-2; i >= 0; i--) {
			if (s[i] > s[i+1]) {
				s[i] = s[i] - 1;
				for (int j = i+1; j < len; j++) s[j] = '9';
			}
		}
		x = 0;
		for (int i = 0; i < len; i++) x = x * 10ll + s[i] - '0';
		printf("Case #%d: %lld\n",++kase,x);
	}
	return 0;
}
