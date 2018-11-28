#define _CRT_SECURE_NO_WARNINGS
#ifdef _MSC_VER
#endif

#include <bits/stdc++.h>
#include <unordered_map>
#include<stack>
using namespace std;
#define OO ll(1e18)
#define MOD ll(100007)
typedef unsigned long long ull;
typedef long long ll;

int check(string s, int k) {
	int ans = 0;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '-' && s.size() - i >= k) {
			ans++;
			for (int j = i; j < i + k; j++) {
				if (s[j] == '-')s[j] = '+';
				else s[j] = '-';
			}
		}
	}
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '-') {
			ans = -1;
			break;
		}
	}
	return ans;
}


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("TextFile1.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		char ar[1111]; int k, ans = 0, ans2 = 0;;
		scanf("%s %d", ar, &k);;
		printf("Case #%d: ", i);
		string s = ar;
		ans = check(s, k);
		reverse(s.begin(), s.end());
		ans2 = check(s, k);
		if (ans == -1 || ans2 == -1)ans = max(ans, ans2);
		if (ans == -1)printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
}