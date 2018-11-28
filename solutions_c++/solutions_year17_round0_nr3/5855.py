#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int> > S;
vector<int> minIsMax() {
	int mxmn = -10;
	vector<int> ret;
	for (int i = 0; i < (int) S.size(); ++i) {
		int l = S[i].first, r = S[i].second;
		if (min(l, r) > mxmn) {
			mxmn = min(l, r);
			ret.clear();
			ret.push_back(i);
		} else if (min(l, r) == mxmn) {
			ret.push_back(i);
		}
	}
	return ret;
}
int maxIsMax(vector<int> minmax) {
	int mxmx = -1;
	vector<int> ret;
	for (int i = 0; i < (int) minmax.size(); ++i) {
		int l = S[minmax[i]].first, r = S[minmax[i]].second;
		if (max(l, r) > mxmx) {
			mxmx = max(l, r);
			ret.clear();
			ret.push_back(minmax[i]);
		} else if (min(l, r) == mxmx) {
			ret.push_back(minmax[i]);
		}
	}
	return ret[0];
}
void Modify(int choose) {
	S[choose].first = S[choose].second = -1;
	for (int i = choose + 1; i < (int) S.size(); ++i) {
		if (S[i].first == -1)
			break;
		S[i].first = i - choose - 1;
	}
	for (int i = choose - 1; i >= 0; --i) {
		if (S[i].first == -1)
			break;
		S[i].second = choose - i - 1;
	}
}

int main() {
	//freopen("C-small-1-attempt0.in", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int Case = 1; Case <= t; ++Case) {
		int n, k;
		scanf("%d%d", &n, &k);
		S.resize(n);
		for (int i = 0; i < n; ++i) {
			S[i].first = i;
			S[i].second = n - i - 1;
		}
		while (--k) {
			Modify(maxIsMax(minIsMax()));
		}
		int doItHere = maxIsMax(minIsMax());
		printf("Case #%d: ", Case);
		printf("%d %d", max(S[doItHere].first, S[doItHere].second),
				min(S[doItHere].first, S[doItHere].second));
		if (Case != t)
			putchar('\n');

	}
	return 0;
}
