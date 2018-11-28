#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int c[10];
char s[1010];
int n;
int ct[] = {-1, 4, -1, 0, -1, 2};
char trs[] = {'R', 'O', 'Y', 'G', 'B', 'V'};

int get(int fst, int lst) {
	if(lst == 0) {
		if(c[2] == c[4]) return fst == 4 ? 4 : 2;
		return c[2] > c[4] ? 2 : 4;
	} else if(lst == 2) {
		if(c[0] == c[4]) return fst == 4 ? 4 : 0;
		return c[0] > c[4] ? 0 : 4;
	} else {
		if(c[0] == c[2]) return fst == 2 ? 2 : 0;
		return c[0] > c[2] ? 0 : 2;
	}
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		bool flag = true;
		scanf("%d", &n);
		for (int i = 0; i < 6; i++) scanf("%d", &c[i]);
		memset(s, 0, sizeof(s));
		int k0 = (bool)c[1], k1 = (bool)c[3], k2 = (bool)c[5];
		if(k0 + k1 + k2 > 1) flag = false;
		int col = k0?1:(k1?3:(k2?5:0));
		int pos = 0, fst ,lst, mc;
		if(col) {
			while(c[col]) {
				if(c[ct[col]]) c[ct[col]]--;
				else flag = false;
				s[pos++] = ct[col];
				c[col]--;
				s[pos++] = col;
			}
			int tot = 0;
			for (int i = 0; i < 6; i++) tot += c[i];
			if(c[ct[col]]) {
				c[ct[col]]--;
				s[pos++] = ct[col];
				fst = lst = ct[col];
			} else if(tot != 0) flag = false;
		} else {
			if(c[0] >= c[2] && c[0] >= c[4]) fst = lst = 0;
			else if(c[2] >= c[0] && c[2] >= c[4]) fst = lst = 2;
			else fst = lst = 4;
			if(c[fst]) {
				c[fst]--;
				s[pos++] = fst;
			}
		}
		//printf("flag %d\n", flag);
		while(c[0] + c[2] + c[4] > 0) {
			if(!flag) break;
			mc = get(fst, lst);
			if(c[mc] <= 0) flag = false;
			s[pos++] = mc;
			c[mc]--;
			lst = mc;
		}
		if(flag) for (int i = 0; i < pos; i++) s[i] = trs[s[i]];
		if(s[n-1] == s[0]) flag = false;
		printf("Case #%d: ", cas);
		if(flag) puts(s);
		else puts("IMPOSSIBLE");
	}
	return 0;
}