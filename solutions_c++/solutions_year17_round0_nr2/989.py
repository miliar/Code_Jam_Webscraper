#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int a[30];
int b[30];
char st[30];
int T, N;
bool _find;

void dfs(int x, int flag) {
	if (x == N) {
		long long ans = 0;
		for (int i=0;i<N;++i)
			ans = ans * 10LL + (long long)a[i];
		printf("%lld\n", ans);
		_find = true;
		return;
	}
	if (flag) {
		a[x] = 9;
		dfs(x + 1, true);
	}
	else {
		if (x == 0 || b[x] >= a[x - 1]) {
			a[x] = b[x];
			dfs(x + 1, false);
		}
		if (_find) return;
		if (x == 0 || b[x] - 1 >= a[x - 1]) {
			a[x] = b[x] - 1;
			dfs(x + 1, true);
		}
		if (_find) return;
	}
}

int main() {
	freopen("B-large.txt", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d\n", &T);
	for (int ii=1;ii<=T;++ii) {
		printf("Case #%d: ", ii);
		scanf("%s", st);
		N = strlen(st);
		for (int i=0;i<N;++i)
			a[i] = b[i] = st[i] - '0';
		_find = false;
		dfs(0, false);
	}
}