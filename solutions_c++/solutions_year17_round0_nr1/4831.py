#include <bits/stdc++.h>

#define N 1000007
#define it(i, n) for(i = 0; i < n; ++i)
#define pb push_back
#define eps 1e-9
#define all(x) x.begin(), x.end() 

using namespace std;
typedef long long ll;

bool check(string s) {
	int i;
	for(i = 0; i < s.size(); ++i) {
		if(s[i] == '-') return false;
	}
	return true;
}

int main(int argc, char * argv[]) {
	int i, j, k, m, n, p, q, r, t;
	string s;

	scanf("%d", &t);

	for(i = 0; i < t; ++i) {
		cin >> s;
		scanf("%d", &k);
		printf("Case #%d: ", i+1);
		m = 0;
		for(j = 0; j <= s.size() - k; ++j) {
			if(s[j] == '-') {
				for(p = j; p < j + k; ++p) {
					if(s[p] == '+') s[p] = '-';
					else s[p] = '+';
				}
				m++;
			}
		}
		if(check(s)) printf("%d\n", m);
		else printf("IMPOSSIBLE\n");

	}

	return 0;
}