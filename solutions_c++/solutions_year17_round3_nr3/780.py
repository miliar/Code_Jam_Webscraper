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
		db u;
		cin >> u;
		vdb p(n);
		vlop(i, p)cin >> p[i];
		sort(all(p));
		reverse(all(p));
		vlop(i, p) {
			db need = 0;
			lop(j, i + 1, n - 1) need +=p[j];
			need = p[i] * (n - i - 1) - need;
			if (need < u) {
				lop(j, i + 1, n - 1) p[j] = p[i];
				u -= need;
				lop(j, i , n - 1) {
					p[j] += (u / (n - i));
				}
				break;
			}
		}
		db ans=1;
		vlop(i, p)ans *= p[i];
		cout << ans << '\n';
	}
	return 0;
}