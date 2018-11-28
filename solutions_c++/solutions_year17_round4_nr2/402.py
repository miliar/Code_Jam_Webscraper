#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define endl "\n"

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;

int cuscnt[1001];
int pos[1001];
int n, c, m;
int prom;
int cnt[1001];

bool test(int ntrains) {
	prom = 0;
	int fre = 0;
	for(int i = 1; i <= n; i++) {
		fre += ntrains;
		if(pos[i] > fre) {
			return false;
		} else {
			fre -= pos[i];
			prom += max(0, pos[i] - ntrains);
		}
	}
	return true;
}

int main(){
	ios_base::sync_with_stdio(0);

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		memset(cuscnt, 0, sizeof cuscnt);
		memset(pos, 0, sizeof pos);

		cin >> n >> c >> m;
		for(int i = 0; i < m; i++) {
			int a, b;
			cin >> a >> b;
			cuscnt[b]++;
			pos[a]++;
		}

		int lo = 0;
		for(int i = 1; i <= c; i++) {
			lo = max(lo, cuscnt[i]);
		}

		int hi = m;
		while(lo < hi) {
			int mid = (lo + hi)/2;
			if(test(mid)) {
				hi = mid;		
			} else {
				lo = mid + 1;
			}
		}

		test(lo);
		cout << "Case #" << t << ": " << lo << " " << prom << endl;
	}
	
	return 0;
}
