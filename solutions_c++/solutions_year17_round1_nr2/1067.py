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

int main() {
	ifstream infile;
	ofstream outfile;
	infile.open("input.txt");
	cin.rdbuf(infile.rdbuf());
	outfile.open("output.txt");
	cout.rdbuf(outfile.rdbuf());
	int t;
	cin >> t;
	lop(testcase, 1, t) {
		int n, p;
		cin >> n >> p;
		vi ing(n);
		vlop(i, ing)cin >> ing[i];
		matrix(int) pack(n, vi(p));
		vlop(i, pack) {
			vlop(j, pack[i])cin >> pack[i][j];
		}
		matrix(ii) limit(n);
		vlop(i, limit) {
			lop(j,0,p-1) {
				int l=int(pack[i][j]/(1.1*ing[i]))-1,u=int(pack[i][j]/(0.9*ing[i]))+1;
				vi range;
				/*cout << l << " "<<u << endl;*/
				lop(k, max(l,1), u) {
					/*cout << 0.9*k*ing[i] << " " << 1.1*k*ing[i] <<" "<<pack[i][j]<< endl;*/
					if (0.9*k*ing[i]<=pack[i][j] && 1.1*k*ing[i]>=pack[i][j])range.pb(k);
				}
				if(sz(range))limit[i].pb(ii(range[0],range.back()));
			}
			sort(all(limit[i]));
			/*vlop(j, limit[i])cout << limit[i][j].first << " " << limit[i][j].second << endl;*/
		}
		int count = 0;
		if (n == 1) count = sz(limit[0]);
		else {
			vrlop(j, limit[0]) {
				ii range = limit[0][j];
				bool empty = false;
				lop(i, 1, n - 1) {
					if (!sz(limit[i])) {
						empty = true;
						break;
					}
				}
				if (empty)break;
				bool found = false;
				lop(i, 1, n - 1) {
					vrlop(k, limit[i]) {
						if (limit[i][k].second < range.first) {
							range = ii(0, 0);
							break;
						}
						else if (limit[i][k].first > range.se) limit[i].pop_back();
						else {
							range.first = max(range.first, limit[i][k].first);
							range.second = min(range.se, limit[i][k].se);
							limit[i].pop_back();
							found = true;
							break;
						}
					}
					if (!found)break;
				}
				if (found)count++;
			}
		}
		cout << "Case #" << testcase << ": " << count<<'\n';
	}
	return 0;
}