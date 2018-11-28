#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>

using namespace std;
int T;
int n, k;
int a[1010];
int main() {
	cin >> T;
	for(int cas = 1; cas <= T; ++cas) {
		string s;
		cin >> s >> k;
		n = s.size();
		for(int i = 0; i < n; ++i) {
			if(s[i] == '+')
				a[i] = 1;
			else 
				a[i] = 0;
		}
		int ans = 0;
		for(int i = 0; i < n; ++i) {
			if(a[i] == 0) {
				if(i + k - 1 >= n) {
					ans = -1;
					break;
				}
				for(int j = i; j <= i + k - 1; ++j) {
					a[j] = 1 - a[j];
				}
				ans++;
			}
		}
		if(ans != -1)
			printf("case #%d: %d\n",cas,ans);
		else 
			printf("case #%d: IMPOSSIBLE\n",cas);
	}
	return 0;
}