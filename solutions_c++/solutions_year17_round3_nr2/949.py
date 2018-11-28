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
		int ac, aj;
		cin >> ac >> aj;
		vi sch(24 * 60 ,0);
		int csum = 0, jsum = 0;
		lop(i, 1, ac) {
			int l, r;
			cin >> l >> r;
			lop(j, l, r-1)sch[j] = -1;
			csum += (r - l);
		}
		lop(i, 1, aj) {
			int l, r;
			cin >> l >> r;
			lop(j, l, r-1)sch[j] = 1;
			jsum += (r - l);
		}
		int p = 0;
		vector<ii> blank;
		while (p < 24 * 60) {
			if (!sch[p]) {
				blank.pb(ii(p, 0));
				while (p<1440) {
					if (sch[p])break;
					p++;
				}
				blank.back().second = p-1;
			}
			else p++;
		}
		if (sz(blank) >= 2) {
			if (blank.back().second == 1439 && blank[0].first == 0) {
				blank[0].first = blank.back().first;
				blank.pop_back();
			}
		}
		int ex = 0;
		vlop(i, blank) {
			int l = blank[i].first, r = blank[i].second;
			if (l > r) {
				if (sch[l - 1] == 1 && sch[r + 1] == 1) {
					if (jsum + (r - l + 1 + 1440)<= 720)jsum += (r - l + 1 + 1440) % 720;
					else ex += 2;
				}
				else if (sch[l-1] == -1 && sch[r+1] == -1) {
					if (csum + (r - l + 1+24 * 60) <= 12 * 60)csum += (r - l + +1+24 * 60);
					else ex += 2;
				}
				else ex++;
			}
			else {
				if (sch[(l - 1 + 1440) % 1440] == 1 && sch[(r + 1) % 1440] == 1) {
					if (jsum + (r - l + 1 )  <= 12 * 60)jsum += (r - l + 1) ;
					else ex += 2;
				}
				else if (sch[(l - 1 + 1440) % 1440] == -1 && sch[(r + 1) % 1440] == -1) {
					if (csum + (r - l + 1)  <= 12 * 60)csum += (r - l +1) ;
					else ex += 2;
				}
				else ex++;
			}
		}
		vlop(i,sch) {
			if (!i) {
				if (sch[i] * sch[1439] < 0)ex++;
			}
			else {
				if (sch[i] * sch[i - 1] < 0)ex++;
			}
		}
		cout << ex << '\n';
	}
	return 0;
}