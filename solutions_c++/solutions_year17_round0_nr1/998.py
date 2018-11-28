#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int Maxn = 1010;

char st[Maxn];
int a[Maxn];
int T, N, K;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	scanf("%d\n", &T);
	for (int ii=1;ii<=T;++ii) {
		scanf("%s %d\n", st, &K);
		N = strlen(st);
		for (int i=0;i<N;++i)
			if (st[i] == '-') a[i] = 0;
			else a[i] = 1;
		int ans = 0;
		for (int i=0;i<N - K + 1;++i)
			if (!a[i]) {
				ans ++;
				for (int j=0;j<K;++j)
					a[i + j] ^= 1;
			}
		bool flag = false;
		for (int i=0;i<N;++i)
			if (!a[i])
				flag = true;
		if (flag) printf("Case #%d: IMPOSSIBLE\n", ii);
		else printf("Case #%d: %d\n", ii, ans);
	}

	return 0;
}