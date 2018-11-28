#include<cstdio>

int T, ans[1005], l;
int n, r, o, y, g, b, v;

void print() {
	for (int i = 0; i < l; i++) switch (ans[i]) {
		case 1: printf("R"); break;
		case 2: printf("O"); break;
		case 3: printf("Y"); break;
		case 4: printf("G"); break;
		case 5: printf("B"); break;
		case 6: printf("V"); break;
	}
	printf("\n");
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	for (int Test = 1; Test <= T; Test++) {
		scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
		int n2 = n, r2 = r, o2 = o, y2 = y, g2 = g, b2 = b, v2 = v;
		l = 0;
		for (int i = 0; i < o; i++) {
			ans[l++] = 5;
			ans[l++] = 2;
			b2--;
			o2--;
			if (i == o - 1 && l != n) {
				ans[l++] = 5;
				b2--;
			}
		}
		if (r - g - 1 > y - v - 1) {
			for (int i = 0; i < g; i++) {
				ans[l++] = 1;
				ans[l++] = 4;
				r2--;
				g2--;
				if (i == g - 1 && l != n || l == n && o != 0) {
					ans[l++] = 1;
					r2--;
				}
			}
			for (int i = 0; i < v; i++) {
				ans[l++] = 3;
				ans[l++] = 6;
				y2--;
				v2--;
				if (i == v - 1 && l != n || l == n && o + g != 0) {
					ans[l++] = 1;
					y2--;
				}
			}
		}
		else {
			for (int i = 0; i < v; i++) {
				ans[l++] = 3;
				ans[l++] = 6;
				y2--;
				v2--;
				if (i == v - 1 && l != n || l == n && o != 0) {
					ans[l++] = 1;
					y2--;
				}
			}
			for (int i = 0; i < g; i++) {
				ans[l++] = 1;
				ans[l++] = 4;
				r2--;
				g2--;
				if (i == g - 1 && l != n || l == n && o + v != 0) {
					ans[l++] = 1;
					r2--;
				}
			}
		}
		if (l == 0) {
			if (r2 >= y2 && r2 >= b2) {
				ans[l++] = 1;
				r2--;
			}
			else if (y2 >= r2 && y2 >= b2) {
				ans[l++] = 3;
				y2--;
			}
			else {
				ans[l++] = 5;
				b2--;
			}
		}
		while (l + 2 < n) {
			if (ans[l - 1] == 1) {
				if (y2 > b2) {
					ans[l++] = 3;
					y2--;
				}
				else {
					ans[l++] = 5;
					b2--;
				}
			}
			else if (ans[l - 1] == 3) {
				if (r2 > b2) {
					ans[l++] = 1;
					r2--;
				}
				else {
					ans[l++] = 5;
					b2--;
				}
			}
			else {
				if (r2 > y2) {
					ans[l++] = 1;
					r2--;
				}
				else {
					ans[l++] = 3;
					y2--;
				}
			}
		}
		if (ans[0] == 1) {
			if (r2) {
				ans[l++] = 1;
				r2--;
			}
		}
		else if (ans[0] == 3) {
			if (y2) {
				ans[l++] = 3;
				y2--;
			}
		}
		else {
			if (b2) {
				ans[l++] = 5;
				b2--;
			}
		}
		while (l < n) {
			if (ans[l - 1] == 1) {
				if (y2 > b2) {
					ans[l++] = 3;
					y2--;
				}
				else {
					ans[l++] = 5;
					b2--;
				}
			}
			else if (ans[l - 1] == 3) {
				if (r2 > b2) {
					ans[l++] = 1;
					r2--;
				}
				else {
					ans[l++] = 5;
					b2--;
				}
			}
			else {
				if (r2 > y2) {
					ans[l++] = 1;
					r2--;
				}
				else {
					ans[l++] = 3;
					y2--;
				}
			}
		}
		printf("Case #%d: ", Test);
		if (r2 < 0 || y2 < 0 || b2 < 0 || ans[0] == ans[l - 1] || ans[l - 2] == ans[l - 3]) printf("IMPOSSIBLE\n");
		else print();
	}
}
