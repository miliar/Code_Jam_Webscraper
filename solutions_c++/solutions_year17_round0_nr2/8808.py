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
	string s;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	TEST(t) {
		cin >> s;
		bitset<500> b;
		b.reset();
		
		forn(i, sz(s)-1){
			if(s[i] > s[i+1]) {
				forr(j, i+1, sz(s)){
					if(b[j])break;
					if(s[j] != 9){
						s[j] = '9';
						b[j] = 1;
					}
				}
				s[i]--;
				i -=2;
			}
		}
		
		bool found = false;
		string aux = "";
		for(int i = 0 ; i < sz(s) ; ++i){
			if(found || s[i] != '0'){
				found = true;
				aux += s[i];
			}
		}
		
		cout << "Case #" << t<< ": " << aux << endl;
	}
}
