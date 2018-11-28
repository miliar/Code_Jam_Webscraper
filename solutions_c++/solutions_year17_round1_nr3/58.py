#include <bits/stdc++.h>
using namespace std;

typedef tuple<int,int,int,int> piiii;

typedef pair<int, piiii> pipiiii;

int N;
int tt = 1;
int ans[105];

mutex mut;

void code() {
		int Hd, Ad, Hk, Ak, B, D;
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

	set<piiii> vis;
	queue<pipiiii> q;
	piiii start(Hd, Ad, Hk, Ak);
	q.push(pipiiii(0, start));
	vis.insert(start);

	while (!q.empty()) {
		int dist;
		int hd, ad, hk, ak;
		pipiiii obj = q.front();
		dist = obj.first;
		tie(hd, ad, hk, ak) = obj.second;
		q.pop();
		if (hd <= 0) continue;

		if (dist == 10000) {
			goto no;
		}
		if (ad >= hk) {
			cout << dist + 1 << endl;
			return;
		}

		#define offer do { if (vis.count(cand) == 0) { q.push(pipiiii(dist+1, cand)); vis.insert(cand); } } while (0)
		piiii cand;
		cand = piiii(hd - ak, ad, hk - ad, ak);
		offer;
		if (B > 0) {
		cand = piiii(hd - ak, ad + B, hk, ak);
		offer;
		}
		cand = piiii(Hd - ak, ad, hk, ak);
		offer;
		if (D > 0) {
		cand = piiii(hd - max((ak-D), 0), ad, hk, max(ak - D, 0));
		offer;
		}
	}
	no:;
	cout << "IMPOSSIBLE\n";
}

int main() {
	cin >> N;
	for (int i = 1; i <= N;i++) {
		cout << "Case #" << i << ": ";
		code();
	}
}
