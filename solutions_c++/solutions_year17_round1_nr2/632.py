#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <iomanip>
#define MOD 1000000007
#define INF 999999999999999
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pl;
typedef vector<ll> vl;
typedef vector<pl > vpl;
typedef vector<vl > vvl;

void solve() {
	ll N, P; cin >> N >> P;
	ll req[N];
	ll maxreq = -1;
	for(int i = 0; i < N; i++) {
		cin >> req[i];
		if(req[i] > maxreq) {
			maxreq = req[i];
		}
	}
	ll packs[N][P+1];
	for(int i = 0; i < N; i++) {
		ll oneingred[P];
		for(int j = 0; j < P; j++) {
			cin >> oneingred[j];
		}
		sort(oneingred, oneingred + P);
		for(int j = 0; j < P; j++) {
			packs[i][j] = oneingred[j];
		}
		packs[i][P] = INF;
	}

	ll pointers[N];
	for(int i = 0; i < N; i++) {
		pointers[i] = 0;
	}
	int ans = 0;
	for(int i = 1; i <= (1200000/maxreq + 1); i++) {
		int is_ok = 1;
		while(is_ok == 1) {
			for(int j = 0; j < N; j++) {
				while(packs[j][pointers[j]] < (9*i*req[j]+9)/10) {
					pointers[j]++;
				}
				if(packs[j][pointers[j]] > (11*i*req[j])/10) {
					is_ok = 0;
				}
			}

			if(is_ok == 1) {
				ans++;
				for(int j = 0; j < N; j++) {
					pointers[j]++;
				}
			}
		}
		// check if it works, for all
		// while currently pointed is too small, increment
		// if currently pointed is too large, impossible
		// if it's okay for all, increment
	}
	cout << ans << endl;
}

int main() {
	ios::sync_with_stdio(false);
	ll T; cin >> T;
	for(int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve(); 
	}
}
