/*
reality, be rent!
synapse, break!
Van!shment Th!s World !!
*/
#include <bits/stdc++.h>
using namespace std;

const int MN = 1010;

//only intended to solve B small. :)

bool vst[MN];
int match[MN];
bool is_good[MN];
vector<int> adj[MN];

bool dfs(int node) {
	for (auto &c : adj[node]) {
		if (!vst[c]) {
			vst[c] = true;
			if (match[c] == -1 || dfs(match[c])) {
				match[c] = node;
				return true;
			}
		}
	}
	return false;
}

int get_match(int asz) {

	int res = 0, i;
	for (i = 0; i < asz; i++) {
		memset(vst, 0, sizeof vst);
		if (dfs(i)) {
			is_good[i] = true;
			res++;
		}
	}
	return res;
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, K = 1;
	scanf("%d", &T);
	while (T--) {
		int n, c, m, i, j;
		scanf("%d %d %d", &n, &c, &m);

		for (i = 0; i < MN; i++) adj[i].clear();
		memset(match, -1, sizeof match);
		memset(is_good, 0, sizeof is_good);

		vector<int> a, b;

		for (i = 0; i < m; i++) {
			int p, B;
			scanf("%d %d", &p, &B);
			if (B == 1) a.emplace_back(p);
			else b.emplace_back(p);
		}

		sort(a.begin(), a.end());
		sort(b.begin(), b.end());

		int asz = a.size(), bsz = b.size();
		for (i = 0; i < asz; i++) {
			for (j = 0; j < bsz; j++) {
				if (a[i] != b[j]) adj[i].push_back(j);
			}
		}

		int ans = get_match(asz);

		vector<int> aa, bb;
		for (i = 0; i < asz; i++) {
			if (!is_good[i]) aa.emplace_back(a[i]);
		}
		for (i = 0; i < bsz; i++) {
			if (match[i] == -1) bb.emplace_back(b[i]);
		}

		asz = aa.size(), bsz = bb.size();
		if (asz == 0 || bsz == 0) {
			ans += asz + bsz;
			printf("Case #%d: %d %d\n", K, ans, 0);
			goto NXT;
		}

		if (aa.back() == 1) {
			ans += asz + bsz;
			printf("Case #%d: %d %d\n", K, ans, 0);
			goto NXT;
		} else {
			ans += max(asz, bsz);
			printf("Case #%d: %d %d\n", K, ans, min(asz, bsz));
			goto NXT;
		}

		NXT:
		K++;
	}
	return 0;
}
