#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

bool spc(int a, string A, int b, string B, int n, string &ans) {
	if (a == b && a + b == n) {
		for (int i = 0; i < a; ++i) {
			ans += A;
			ans += B;
		}
		return true;
	}
	return false;
}

bool makeThree(int a, string A, int b, string B, int c, string C, string &ans) {
	int n = a + b + c;
	if (max(max(a, b), c) > n / 2) {
		return false;
	}
	for (int i = 0; i < n; ++i) {
		ans += " ";
	}
	if (b > a) {
		swap(a, b);
		swap(A, B);
	}
	if (c > a) {
		swap(c, a);
		swap(C, A);
	}
	for (int i = 0; i < n; i += 2) {
		if (a) {
			ans[i] = A[0];
			--a;
		} else if (b) {
			ans[i] = B[0];
			--b;
		} else if (c) {
			ans[i] = C[0];
			--c;
		}
		if (i + 2 >= n && i % 2 == 0) {
			i = 1 - 2;
		}
	}
	return true;
}

void addType(string A, int a, string T, string &ans) {
	if (a) {
		string TT = "";
		for (int i = 0; i < a; ++i) {
			TT += T;
		}
		TT += A;
		ans.replace(ans.find_first_of(A), 1, TT);
	}
}

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		int n, r, o, y, g, b, v;
		scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
		vector<string> tans;
		string ans;
		if (o > b || g > r || v > y) {
			ans = "IMPOSSIBLE";
		} else {
			//Special cases
			if (!spc(o, "O", b, "B", n, ans) && 
				!spc(g, "G", r, "R", n, ans) &&
				!spc(v, "V", y, "Y", n, ans)) {
				if (makeThree(b - o, "B", r - g, "R", y - v, "Y", ans)) {
					addType("B", o, "BO", ans);
					addType("R", g, "RG", ans);
					addType("Y", v, "YV", ans);
				} else {
					ans = "IMPOSSIBLE";
				}
			}
		}
		static int id = 0;
		printf("Case #%d: %s\n", ++id, ans.c_str());
	}
	return 0;
}
