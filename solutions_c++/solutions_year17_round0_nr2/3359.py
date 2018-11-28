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
	ifstream ifs("B-large.in");
	ofstream ofs("B2.txt");

	int T;
	ifs >> T;
	vs n(T);
	rep(i, T) {
		ifs >> n[i];
	}
	rep(i, T) {
		ofs << "Case #" << i + 1 << ": ";
		int dec = -1;
		int left = 0;
		rep(j, n[i].length() - 1) {
			if (n[i][j] > n[i][j + 1]) {
				dec = j;
				break;
			}
		}
		if (dec == -1) {
			ofs << n[i] << endl;
			continue;
		}
		if (n[i][dec] == '1') {
			rep(j, n[i].length() - 1) {
				ofs << 9;
			}
			ofs << endl;
			continue;
		}
		replrev(j, 1, dec + 1) {
			if (n[i][j] != n[i][j - 1]) {
				left = j;
				break;
			}
		}
		rep(j, n[i].length()) {
			if (j < left) {
				ofs << n[i][j];
			}
			else if (j == left) {
				ofs << (int)(n[i][j] - '0') - 1;
			}
			else {
				ofs << 9;
			}
		}
		ofs << endl;
	}

	return 0;
}