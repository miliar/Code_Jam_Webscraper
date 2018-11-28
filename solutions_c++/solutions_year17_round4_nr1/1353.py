#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;

const int MaxN = 1000;
int n, P, T;
int a[MaxN + 5], cnt[MaxN + 5];

void Init()
{
	scanf("%d%d", &n, &P);
	memset(cnt, 0, sizeof(cnt));
	for (int i = 1; i <= n; i++) {
		scanf("%d", &a[i]);	
		a[i] %= P;
		cnt[a[i]]++;
	}
}

void Solve(int cas)
{
	int ans;
	if (P == 1) {
		ans = n;
	}	
	else if (P == 2) {
		ans = cnt[0] + (cnt[1] + 1) / 2;
	}
	else if (P == 3) {
		int MiN = min(cnt[1], cnt[2]);
		int MaX = max(cnt[1], cnt[2]);
		ans = cnt[0] + MiN + (MaX - MiN + 2) / 3;
	}
	else if (P == 4) {
		int MiN = min(cnt[1], cnt[3]);
		ans = cnt[0] + cnt[2] / 2 + MiN; 
		cnt[2] %= 2; cnt[1] -= MiN; cnt[3] -= MiN;
		int temp = max(cnt[1], cnt[3]);
		if (cnt[2] == 1 && (temp >= 2)) {
			ans++;
			cnt[2] = 0;
			temp -= 2;
		}
		ans += (temp + cnt[2] + 3) / 4;
		ans = max(ans, 1);
	}
	printf("Case #%d: %d\n", cas, ans);
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
	//freopen("A-small-attempt2.in", "r", stdin); freopen("A-small-attempt2.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		Init();
		Solve(i);
	}
	fclose(stdin); fclose(stdout);
}
