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
	ifstream ifs("B1.in");
	ofstream ofs("B1.txt");
	cin.rdbuf(ifs.rdbuf());
	cout.rdbuf(ofs.rdbuf());
	//*/

	int T;
	cin >> T;
	rep(t, T) {
		int N, C, M;
		cin >> N >> C >> M;
		vi p(M), b(M);
		vvi pb(N);
		rep(i, N)pb[i] = vi(C, 0);

		rep(i, M) {
			cin >> p[i] >> b[i];
			p[i]--;
			b[i]--;
			pb[p[i]][b[i]]++;
		}
		//C=2
		int ride = 0, promote = 0;
		int sum0 = 0, sum1 = 0;
		repl(i, 1, N) {
			sum0 += pb[i][0];
			sum1 += pb[i][1];
		}
		
		if (pb[0][0] > sum1&&pb[0][1] > sum0) {
			ride = pb[0][0] + pb[0][1];
			promote = 0;
		}
		else {
			ride = max(pb[0][0] + sum0, pb[0][1] + sum1);
			if (pb[0][0] < sum1&&pb[0][1] < sum0) {
				sum0 += pb[0][0];
				sum1 += pb[0][1];
				int max0 = 0, maxid = 0;
				rep(i, N) {
					if (min(pb[i][0], pb[i][1]) > max0) {
						max0 = min(pb[i][0], pb[i][1]);
						maxid = i;
					}
				}
				promote = max(0, min(pb[maxid][1] - (sum0 - pb[maxid][0]), pb[maxid][0] - (sum1 - pb[maxid][1])));
			}
			else {
				promote = 0;
			}
		}
		cout << "Case #" << t + 1 << ": " << ride << ' ' << promote << endl;
	}


	return 0;
}