#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i = (a); i < (b); i++)
#define iter(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end();++it)
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int INF = ~(1<<31);
const double pi = acos(-1);


int main() {
	cin.sync_with_stdio(false);
	ofstream fout("a.ans");
	int t;
	cin >> t;
	rep(u,0,t) {
		int n,k;
		cin >> n >> k;
		long double mx = 0;
		vector<pair<long double,long double>> st(n);
		rep(i,0,n) cin >> st[i].first >> st[i].second;
		sort(st.rbegin(), st.rend());
		rep(i,0,n-k+1) {
			vii pick;
			long double cansee = 2*pi*st[i].first*st[i].second;
			cansee += pi*(st[i].first*st[i].first);
			vector<long double> oth;
			rep(a,i+1, n) {
				long double m = 2*pi*st[a].first*st[a].second;
				oth.push_back(m);
			}
			sort(oth.rbegin(), oth.rend());
			rep(a,0,k-1) cansee += oth[a];
			mx = max(mx, cansee);
		}
		fout << setprecision(15) << fixed <<  "Case #" << u+1 << ": " << mx << endl;
	} 
	return 0;
}

