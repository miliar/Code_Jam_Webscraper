#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second

typedef long long ll;
typedef pair<int, int> ii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

int hd, ad;
int hk, ak;
int b, d;
int dist[101][201][101][101];

int go () {
	memset (dist, INF, sizeof dist);

	queue <tuple <int, int, int, int> > q;
	q.emplace(hd, ad, hk, ak);
	dist[hd][ad][hk][ak] = 0;

	while (q.size()) {
		int vd, dd, vk, dk;
		tie (vd, dd, vk, dk) = q.front();
		q.pop();
		int dt = dist[vd][dd][vk][dk];

		if (!vk)
			return dt;

		// curar
		if (hd - dk > 0) {
			if (dist[hd - dk][dd][vk][dk] > dt + 1) {
				dist[hd - dk][dd][vk][dk] = dt + 1;
				q.emplace(hd - dk, dd, vk, dk);
			}
		}

		// atacar
		int vidak = max (vk - dd, 0);
		if (!vidak) {
			return dt + 1;
		}
		if (vd - dk > 0 and dist[vd - dk][dd][vidak][dk] > dt + 1) {
			dist[vd - dk][dd][vidak][dk] = dt + 1;
			q.emplace(vd - dk, dd, vidak, dk);
		}

		// buff
		if (vd - dk > 0 and dd + b <= 200) {
			if (dist[vd - dk][dd + b][vk][dk] > dt + 1) {
				dist[vd - dk][dd + b][vk][dk] = dt + 1;
				q.emplace(vd - dk, dd + b, vk, dk);
			}
		}

		// debuff
		int danok = max (dk - d, 0);
		if (vd - danok > 0 and dist[vd - danok][dd][vk][danok] > dt + 1) {
			dist[vd - danok][dd][vk][danok] = dt + 1;
			q.emplace(vd - danok, dd, vk, danok);
		}
	}
	
	return -1;
}

int main (void) {
	ios_base::sync_with_stdio(false);

	int T;	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> hd >> ad >> hk >> ak >> b >> d;

		int res = go ();

		cout << "Case #" << t << ": ";
		if (res == -1)	cout << "IMPOSSIBLE" << endl;
		else			cout << res << endl;
	}

	return 0;
}
