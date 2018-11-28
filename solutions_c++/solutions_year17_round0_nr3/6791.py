#include <bits/stdc++.h>

#define si(n) scanf("%d", &n)
#define sii(n, m) scanf("%d %d", &n, &m)
#define sc(c) scanf("%c", &c)
#define ss(s) scanf("%s", s)

#define forn(i, n) for(int i = 0 ; i < n ; ++i)
#define forr(i, a, b) for(int i = a ; i < b ; ++i)

#define sz(x) (int)x.size()

#define rforn(i, n) for(int i = n-1 ; i >= 0 ; --i)
#define rforr(i, a, b) for(int i = b-1 ; i >= a ; --i)

#define mset(x, y) memset(x, y, sizeof(x))
#define all(x) x.begin(), x.end()

#define TEST(t) int T; cin >> T; for(int t = 1 ; t <= T ; ++t)

#ifdef ONLINE_JUDGE
	#define sll(x) scanf("%I64d", &x)
#else
	#define sll(x) cin >> x
#endif

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

typedef complex<double> cd;

typedef vector<int> vi;
typedef vector<cd> vcd;


int main(){
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);
	TEST(t){
		int n, k;
		sii(n, k);
		vector<int> l(n,0), r(n, 0);
		l[0] = r[n-1] = 0;
		forr(i, 1, n)l[i] = l[i-1] + 1;
		rforr(i, 0, n-1)r[i] = r[i+1] + 1;
		
		int index;
		pair<int, int> p;
		bitset<100000> b;
		b.reset();
		
		while(k-- > 0){
			p = make_pair(-1, -1);
			index = -1;
			forn(i, n){
				if(b[i])continue;
				int mini1 = min(l[i], r[i]);
				int maxi1 = max(l[i], r[i]);
				int mini2 = min(p.first, p.second);
				int maxi2 = max(p.first, p.second);
				
				if( mini1 > mini2){
					index = i;
					p = make_pair(l[i], r[i]);
				}
				else if(mini1 == mini2 && maxi1 > maxi2){
					index = i;
					p = make_pair(l[i], r[i]);
				}
			}
			b[index] = 1;
			l[index] = -1;
			r[index] = -1;
			forr(i, index+1, n){
				if(b[i])break;
				l[i] = l[i-1] + 1;
			}
			rforr(i, 0, index){
				if(b[i])break;
				r[i] = r[i+1] + 1;
			}
		}
		
		cout << "Case #" << t << ": " << max(p.first, p.second) << " " << min(p.first, p.second) << "\n";
	}
}
