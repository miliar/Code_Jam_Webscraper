#include "bits/stdc++.h"
#include <sys/timeb.h>
#include <fstream>

using namespace std;

#define repl(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define rep(i,n) repl(i,0,n)
#define replrev(i,a,b) for(int i=(int)(b)-1;i>=(int)(a);i--)
#define reprev(i,n) replrev(i,0,n)
#define repi(itr,ds) for(auto itr = ds.begin(); itr != ds.end(); ++itr)
#define all(a) a.begin(),a.end()
#define mp make_pair
#define INF 2000000000
#define INFL 1000000000000000000LL
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

int main() {
	//*
	ifstream ifs("A2.in");
	ofstream ofs("A2.txt");
	cin.rdbuf(ifs.rdbuf());
	cout.rdbuf(ofs.rdbuf());
	//*/

	int T;
	cin >> T;
	rep(t, T) {
		int N, P;
		cin >> N >> P;
		vi g(N);
		vi m(P, 0);
		rep(i, N) {
			cin >> g[i];
			m[g[i] % P]++;
		}
		int ans = m[0];
		if (P == 2) {
			ans += (m[1] + 1) / 2;
		}
		else if (P == 3) {
			int minimum = min(m[1], m[2]);
			ans += minimum;
			//if (m[1] == m[2])ans--;
			m[1] -= minimum;
			m[2] -= minimum;
			if (m[1] > 0) {
				ans += (m[1] + 2) / 3;
			}
			else if (m[2] > 0) {
				ans += (m[2] + 2) / 3;
			}
		}
		else if (P == 4) {
			int minimum = min(m[1], m[3]);
			ans += minimum;
			m[1] -= minimum;
			m[3] -= minimum;
			ans += m[2] / 2;
			m[2] %= 2;
			if (m[2] > 0) {
				if (m[1] > 0) {
					int min2 = min(m[1] / 2, m[2]);
					ans += min2;
					m[1] -= min2 * 2;
					m[2] -= min2;
					if (m[1] > 0) {
						ans += (m[1] + 3) / 4;
					}
					else if (m[2] > 0) {
						ans += (m[2] + 3) / 4;
					}
				}
				else if (m[3] > 0) {
					int min2 = min(m[3] / 2, m[2]);
					ans += min2;
					m[3] -= min2 * 2;
					m[2] -= min2;
					if (m[3] > 0) {
						ans += (m[3] + 3) / 4;
					}
					else if (m[2] > 0) {
						ans += (m[2] + 3) / 4;
					}
				}
				else if (m[2] > 0) {
					ans++;
				}
			}
			else {
				if (m[1] > 0) {
					ans += (m[1] + 3) / 4;
				}
				else if (m[3] > 0) {
					ans += (m[3] + 3) / 4;
				}
			}
		}

		cout << "Case #" << t + 1 << ": " << ans << endl;
	}


	return 0;
}