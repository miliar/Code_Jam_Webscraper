#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#define ll long long
using namespace std;

int T;
int s[30], res[30];
ll n;

bool dfs(int pos, int u, int lx) {
	if(pos == -1) return true;
	int R = u ? s[pos] : 9;
	for (int i = R; i >= lx; i--) {
		res[pos] = i;
		if(dfs(pos-1, u&&(i==s[pos]), i)) return true;
	}
	return false;
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		cin >> n;
		int len = 0;
		while(n) {
			s[len] = n % 10;
			n /= 10;
			len++;
		}
		printf("Case #%d: ", cas);
		dfs(len-1, 1, 0);
		ll ret = 0;
		for(int i = len-1; i >= 0; i--) ret = ret*10+res[i];
		cout << ret << endl;
	}
	return 0;
}