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



int main() {
	ifstream ifs("A2.in");
	ofstream ofs("A2.txt");

	int T;
	ifs >> T;
	rep(t, T) {
		int R, C;
		ifs >> R >> C;
		vvc c(R);
		rep(i, R) {
			c[i] = vc(C);
			string str;
			ifs >> str;
			rep(j, C) {
				c[i][j] = str[j];
			}
		}
		vb isnull(R, true);
		vi left(R);
		int top = INF, bottom = -1;
		rep(i, R) {
			rep(j, C) {
				if (c[i][j] != '?') {
					isnull[i] = false;
					left[i] = j;
					top = min(top, i);
					bottom = max(bottom, i);
					break;
				}
			}
		}
		rep(i, R) {
			if (isnull[i])continue;
			rep(j, C) {
				if (j < left[i]) {
					c[i][j] = c[i][left[i]];
				}
				else {
					if (c[i][j] == '?') {
						c[i][j] = c[i][j - 1];
					}
				}
			}
		}
		rep(i, R) {
			if (!isnull[i])continue;
			if (i < top) {
				rep(j, C) {
					c[i][j] = c[top][j];
				}
			}
			else if (i > bottom) {
				rep(j, C) {
					c[i][j] = c[bottom][j];
				}
			}
			else {
				rep(j, C) {
					c[i][j] = c[i - 1][j];
				}
			}
		}

		ofs << "Case #" << t + 1 << ":" << endl;
		rep(i, R) {
			rep(j, C) {
				ofs << c[i][j];
			}
			ofs << endl;
		}
	}

	return 0;
}