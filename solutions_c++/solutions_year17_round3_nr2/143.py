#include<bits/stdc++.h>
using namespace std;
const bool DBG = 1;

#define TRACE(x)    x
#define WATCH(x)    TRACE(cout << #x" = " << x << endl)
#define WATCHR(a,b) TRACE(for(auto it=a; it!=b;) cout<<*(it++)<<" ";cout<<endl)
#define WATCHC(V)   TRACE({cout << #V" = "; WATCHR(V.begin(), V.end());})
#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<pair<int,int>> vpii;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	cout << fixed << setprecision(15);

	int T, Ac, Aj, s, e;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cin >> Ac >> Aj;
		int N = Ac + Aj;
		vector<pair<pair<int, int>, int>> all;
		int tc=720, tj=720;
		for(int i = 0; i < Ac; i++) {
			cin >> s >> e;
			all.push_back( {{s,e},0} );
			tc -= e-s;
		}
		for(int i = 0; i < Aj; i++) {
			cin >> s >> e;
			all.push_back( {{s,e},1} );
			tj -= e-s;
		}
		sort(all.begin(), all.end());
		vector<pair<pair<int, int>, int>> segs;
		for(int i = 0; i < N; i++) {
			segs.push_back(all[i]);
			int s = all[i].first.second;
			int e = all[(i+1)%N].first.first;
			if(e<s) e += 1440;
			int v = (all[i].second == all[(i+1)%N].second)? all[i].second+2 : 4;
			segs.push_back( {{s,e}, v} );
		}

		/*for(auto seg : segs) {
			cout << seg.first.first << "-" << seg.first.second << " => " << seg.second << endl;
		}*/

		while(tc > 0 || tj > 0) {
			bool chg = 0;
			int smallest = 10000;
			int ix = -1;
			for(int i = 0; i < segs.size(); i++) {
				int s = segs[i].first.first;
				int e = segs[i].first.second;
				if(segs[i].second == 2 && (e - s < smallest)) {
					smallest = e-s;
					ix = i;
				}
			}
			if(ix != -1 && smallest <= tc) {
				chg = 1;
				segs[ix].second = 0;
				tc -= smallest;
			}

			smallest = 10000;
			ix = -1;
			for(int i = 0; i < segs.size(); i++) {
				int s = segs[i].first.first;
				int e = segs[i].first.second;
				if(segs[i].second == 3 && (e - s < smallest)) {
					smallest = e-s;
					ix = i;
				}
			}
			if(ix != -1 && smallest <= tj) {
				chg = 1;
				segs[ix].second = 1;
				tj -= smallest;
			}
			if(!chg) break;
		}

		int result = 0;
		for(auto seg : segs) {
			int s = seg.first.first;
			int e = seg.first.second;
			int v = seg.second;
			if(e-s > 0 && (v == 2 || v == 3)) result += 2;
			if(v == 4) result += 1;
		}

		cout << result << endl;
	}

	return 0;
}
