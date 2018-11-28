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
	ifstream ifs("C-small-2-attempt0.in");
	ofstream ofs("C2.txt");

	int T;
	ifs >> T;
	rep(i, T) {
		int N, K;
		ifs >> N >> K;
		ofs << "Case #" << i + 1 << ": ";

		priority_queue<pair<ll,ll>> q;
		q.push(mp(N, 1));
		ll sum = 0;
		while (true) {
			ll num = q.top().first;
			ll count = q.top().second;
			q.pop();
			while (!q.empty() && q.top().first == num) {
				count += q.top().second;
				q.pop();
			}
			sum += count;
			if (sum >= K) {
				ofs << num / 2 << ' ' << (num - 1) / 2 << endl;
				break;
			}
			q.push(mp(num / 2, count));
			q.push(mp((num - 1) / 2, count));
		}
	}

	return 0;
}