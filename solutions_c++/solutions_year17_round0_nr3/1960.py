#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef pair< ii , int > pii;
#define endl '\n'
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ll long long
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(decltype((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define FASTIO (ios_base::sync_with_stdio(0),cout.tie(0),cin.tie(0))
#define TIME_S clock_t tStart = clock()
#define TIME_E printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC)
const int INF = 1e9;
/*codejam_2017_C_Q*/

int main() {
	FASTIO;
	int t;
	cin >> t;
	REP(c, t) {
		ll n, k;
		cin >> n >> k;
		ll max = n / 2, min = (n - 1) / 2;
		k--;
		ll x = max, y = min;
		ll i = 1;
		map< ll, ll > s;
		s[x]++;
		s[y]++;
		while (k > 0) {
			auto it = s.end();
			it--;
			ll tmp = it->first;
			if (k > it->second) {
				k -= it->second;
				s[tmp / 2] += it->second;
				s[(tmp - 1) / 2] += it->second;
				s.erase(it);
			}
			else {
				k = 0;
				max = tmp / 2;
				min = (tmp - 1) / 2;
			}
		}
		cout << "Case #" << c + 1 << ": " << max << " " << min << endl;
	}
}
