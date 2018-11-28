#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <string>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <numeric>

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef long long ll;
typedef pair<long long, long long> l4;
typedef vector<long long> vll;
typedef double db;
typedef vector<double> vdb;
typedef pair<double, double> dd;
typedef set<int> si;
typedef set<long long> sll;
#define fi first
#define se second
#define matrix(a) vector< vector<a> >
#define sz(a) int((a).size()) 
#define lop(i,a,b) for (int i=a; i<=b; i++)
#define vlop(i,v) lop(i,0,sz(v)-1)
#define vlop1(i,v) lop(i,1,sz(v)-1)
#define rlop(i,a,b) for (int i=b; i>=a; i--)
#define vrlop(i,v) rlop(i,0,sz(v)-1)
#define vrlop1(i,v) rlop(i,1,sz(v)-1)
#define printv(i,v) vlop(i,v)cout<<v[i]<<" "
#define printv1(i,v) vlop1(i,v)cout<<v[i]<<" "
#define all(s) (s).begin(),(s).end()
#define pb push_back
#define enter cout<<'\n'
#define lb(i,v) int(lower_bound(all(v),i)-v.begin())
#define ub(i,v) int(upper_bound(all(v),i)-v.begin())
const long double pi = acos(-1.0);
int main() {
	ifstream infile;
	ofstream outfile;
	infile.open("input.txt");
	cin.rdbuf(infile.rdbuf());
	outfile.open("output.txt");
	cout.rdbuf(outfile.rdbuf());
	cout << setprecision(8) << fixed;
	int t;
	cin >> t;
	lop(testcase, 1, t) {
		cout << "Case #" << testcase << ": ";
		int n, k;
		cin >> n >> k;
		vi r(n), h(n);
		vlop(i, r)cin >> r[i] >> h[i];
		vector< pair<ll, int> > pc(n);
		vlop(i, pc) {
			pc[i].first = 1LL*r[i] * h[i]*2;
			pc[i].second = i;
		}
		sort(all(pc));
		reverse(all(pc));
		ll maxs = -1;
		vlop(i, r) {
			int count = 1;
			ll s = 1LL*r[i]*r[i]+1LL*r[i]*h[i]*2;
			vlop(j, pc) {
				if (count == k)break;
				if (r[pc[j].se] <= r[i]&&pc[j].second!=i) {
					count++;
					s +=pc[j].first;
				}
			}
			if (count == k)maxs = max(maxs, s);
		}
		cout << pi*maxs << '\n';
	}
	return 0;
}