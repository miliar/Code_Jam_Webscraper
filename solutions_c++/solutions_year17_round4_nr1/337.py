#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <map>
#include <vector>

using namespace std;

const int H = 101;

int mod[4], a[H], n, p;
map<int, int> M;

int h(int a1, int a2, int a3, int res) {
	return ((a1 * H + a2) * H + a3) * 4 + res;
}

int search(int a1, int a2, int a3, int res) {
	if (!a1 && !a2 && !a3) return 0;
	int hval = h(a1, a2, a3, res);
	if (M.find(hval) != M.end())
		return M.find(hval)->second;
	int ans = 0, t = (res == 0 ? 1 : 0);
	if (a1 > 0) {
		int v1 = t + search(a1 - 1, a2, a3, (res + 3) & 3);
		ans = max(ans, v1);
	}
	if (a2 > 0) {
		int v2 = t + search(a1, a2 - 1, a3, (res + 2) & 3);
		ans = max(ans, v2);
	}
	if (a3 > 0) {
		int v3 = t + search(a1, a2, a3 - 1, (res + 1) & 3);
		ans = max(ans, v3);
	}
	M.insert(make_pair(hval, ans));
	return ans;
}

void run(int cas) {
	scanf("%d%d", &n, &p);
	for (int i = 0; i < n; i++)
		scanf("%d", a + i);
	memset(mod, 0, sizeof(mod));
	for (int i = 0; i < n; i++)
		mod[a[i] % p] += 1;
	if (p == 2) {
		int odd = mod[1], even = mod[0];
		printf("Case #%d: %d\n", cas, even + (odd + 1) / 2);
		return;
	}
	if (p == 3) {
		int ans = mod[0];
		while (mod[1] >=3 && mod[1] > mod[2] + 1) {
			ans++;
			mod[1] -= 3;
		}
		while (mod[2] >=3 && mod[2] > mod[1] + 1) {
			ans++;
			mod[2] -= 3;
		}
		int x = min(mod[1], mod[2]);
		ans += x + ((mod[1] > x || mod[2] > x) ? 1 : 0);
		printf("Case #%d: %d\n", cas, ans);
		return;
	}
	if (p == 4) {
		int ans = search(mod[1], mod[2], mod[3], 0) + mod[0];
		printf("Case #%d: %d\n", cas, ans);
	}
}

int main() {
	int cas, tt;
	scanf("%d", &tt);
	for (cas = 1; cas <= tt; cas++)
		run(cas);
	return 0;
}
