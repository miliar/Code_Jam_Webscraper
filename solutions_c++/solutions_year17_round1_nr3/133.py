#include <bits/stdc++.h>

using namespace std;

// [Hd][Ad][Hk][Ak]
int F[101][101][101][101];

int main(void)
{
	int T = 0;
	int TK = 0;
	cin >> T;
	while (T--) {
		memset(F, 0x3F, sizeof(F));
		int Hd, Ad, Hk, Ak, B, D;
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		int ans = ~0U>>1;
		queue<tuple<int, int, int, int>> q;
		q.push({Hd, Ad, Hk, Ak});
		F[Hd][Ad][Hk][Ak] = 0;
		auto probe = [&](int nHd, int nAd, int nHk, int nAk, int cv) {
			if (nAd > 100) nAd = 100;
			if (nAk < 0) nAk = 0;

			if (nHk <= 0) ans = min(ans, cv + 1);
			else {
				nHd -= nAk;
				if (nHd <= 0) {
					// lose
				} else if (F[nHd][nAd][nHk][nAk] > cv + 1) {
					F[nHd][nAd][nHk][nAk] = cv + 1;
					q.push({nHd, nAd, nHk, nAk});
				}
			}
		};
		while (!q.empty()) {
			int cHd, cAd, cHk, cAk;
			tie(cHd, cAd, cHk, cAk) = q.front(); q.pop();
			int cv = F[cHd][cAd][cHk][cAk];
			probe(cHd, cAd, cHk - cAd, cAk, cv); // Attack
			probe(cHd, cAd + B, cHk, cAk, cv); // Buff
			probe(Hd, cAd, cHk, cAk, cv); // Cure
			probe(cHd, cAd, cHk, cAk - D, cv); // Debuff
		}
		cout << "Case #" << ++TK << ": ";
		if (ans > 0x3f000000) cout << "IMPOSSIBLE";
		else cout << ans;
		cout << endl;
	}
	return 0;
}
