#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<pii> vii;
typedef vector<bool> vb;
typedef vector<string> vs;
const int di[] = { -1,0,1,0 };
const int dj[] = { 0,1,0,-1 };
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
#define mp make_pair

int main() {
	ios::sync_with_stdio(false), cin.tie(0);
	ifstream cin("B-small-attempt0.in");
	ofstream cout("output.txt");
	int t, tt = 0; cin >> t;
	while (t--) {
		int n, cc, m; cin >> n >> cc >> m;
		vvi tr, otr;
		vector<vb> trp, otrp;
		for (int i = 0; i < m; i++) {
			int p, b; cin >> p >> b;
			int c = 0;
			while (c < tr.size() && (tr[c][p] || trp[c][b])) c++;
			if (c == tr.size()) {
				tr.push_back(vi(1005));
				trp.push_back(vb(1005));
			}
			tr[c][p] = b;
			trp[c][b] = true;
		}

		int r = 0;
		for (int i = tr.size() - 1; i > 0; i--) {
			otr = tr, otrp = trp;
			int cp = 0;

			for (int j = 1; j < tr[i].size(); j++) {
				if (tr[i][j] == 0) continue;

				for (int k = 0; k < tr.size(); k++) {
					if (trp[k][tr[i][j]]) continue;

					int c = 1;
					while (c <= n && tr[k][c] && c < j) c++;
					if (c <= n && c < j) {
						tr[k][c] = tr[i][j];
						trp[k][tr[i][j]] = true;
						trp[i][tr[i][j]] = false;
						tr[i][j] = 0;
						cp++;
						break;
					}
				}
			}

			bool emp = true;
			for (int j = 1; j < tr[i].size(); j++)
				if (tr[i][j]) {
					emp = false;
					tr = otr, trp = otrp; break;
				}
			if (emp) {
				tr.erase(tr.begin() + i), trp.erase(trp.begin() + i);
				otr = tr, otrp = trp;
				r += cp;
			}
		}

		cout << "Case #" << ++tt << ": ";
		cout << tr.size() << " " << r << endl;
	}
	//cin.ignore(), cin.get();
}
