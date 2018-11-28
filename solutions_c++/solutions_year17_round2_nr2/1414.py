#include <bits/stdc++.h>
using namespace std;

int main() {

	freopen("readin.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	while (t--) {
		int n;
		scanf("%d", &n);
		string ans;
		ans.resize(n, ' ');
		int ch[] = { 'R', 'O', 'Y', 'G', 'B', 'V' };
		int f[6] = { 0 };
		vector<char> v;
		vector<pair<int, int> > ord;
		for (int i = 0; i < 6; i++) {
			scanf("%d", &f[i]);
			ord.push_back(make_pair(f[i], i));
		}
		sort(ord.begin(), ord.end());

		for (int i = 0; i < ord.size(); i++) {
			int x = ord[i].first;
			int in = ord[i].second;
			while (x) {
				x--;
				v.push_back(ch[in]);
			}
		}

		int ct = 0;
		while (v.size()) {
			ans[ct] = v.back();
			v.pop_back();
			ct += 2;
			if (ct >= n)
				ct = 1;
		}
		bool imp = false;
		for (int i = 0; i < n; i++) {
			int l = (i - 1 + n) % n;
			int r = (i + 1) % n;
			if (ans[i] == ans[l] || ans[i] == ans[r])
				imp = true;
		}
		static int tc = 1;
		if (!imp)
			printf("Case #%d: %s\n", tc++, ans.c_str());
		else
			printf("Case #%d: IMPOSSIBLE\n", tc++);
	}

	return 0;
}
