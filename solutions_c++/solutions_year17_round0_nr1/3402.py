#include "bits/stdc++.h"
#include <sys/timeb.h>
#include <fstream>

using namespace std;

#define repl(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define rep(i,n) repl(i,0,n)
#define replrev(i,a,b) for(int i=(int)(b)-1;i>=(int)(a);i--)
#define reprev(i,n) replrev(i,0,n)
#define repi(itr,ds) for(auto itr = ds.begin(); itr != ds.end(); ++itr)
#define mp make_pair
#define INF 2000000000
#define INFL 2000000000000000000LL
#define EPS 1e-9
#define MOD 1000000007
#define PI 3.1415926536
#define RMAX 4294967295

//#define DEBUG

#ifdef DEBUG
#define dprintf printf
#define dbg 
#define drepl(i,a,b) repl(i,a,b)
#define drep(i,n) rep(i,n)
#else
#define dprintf (true)?0:printf
#define dbg if(false)
#define drepl(i,a,b) int i; if(false)
#define drep(i,n) int i; if(false)
#endif // DEBUG


typedef long long ll;
typedef pair<int, int> P;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<bool> vb;
typedef vector<char> vc;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<P> vP;
typedef vector<vector<int> > vvi;
typedef vector<vector<bool> > vvb;
typedef vector<vector<ll> > vvll;
typedef vector<vector<char> > vvc;
typedef vector<vector<double> > vvd;
typedef vector<vector<P> > vvP;
typedef priority_queue<int, vector<int>, greater<int> > pqli;
typedef priority_queue<ll, vector<ll>, greater<ll> > pqlll;
typedef priority_queue<P, vector<P>, greater<P> > pqlP;
typedef pair<int, pair<int, int> > Edge;
typedef vector<Edge> vE;
typedef priority_queue<Edge, vector<Edge>, greater<Edge> > pqlE;


int main() {
	ifstream ifs("A-large.in");
	ofstream ofs("A.txt");

	int T;
	ifs >> T;
	vs s(T);
	vi k(T);
	rep(i, T) {
		ifs >> s[i] >> k[i];
	}

	rep(i, T) {
		int ans = 0;
		vi num(s[i].length() + 1, 0);
		int rev = 0;
		rep(j, s[i].length() - k[i] + 1) {
			rev += num[j];
			if (s[i][j] == (rev % 2 == 0 ? '-' : '+')) {
				num[j + 1]++;
				num[min((int)s[i].length(), j + k[i])]--;
				ans++;
			}
		}
		bool possible = true;
		repl(j, s[i].length() - k[i] + 1, s[i].length()) {
			rev += num[j];
			if (s[i][j] == (rev % 2 == 0 ? '-' : '+')) {
				possible = false;
				break;
			}
		}
		ofs << "Case " << "#" << i + 1 << ": ";
		if (possible) {
			ofs << ans << endl;
		}
		else {
			ofs << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}