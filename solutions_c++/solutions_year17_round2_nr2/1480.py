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

const db eps = 1e-11;

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
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		cout << "Case #" << testcase << ": ";
		if (r > n / 2 || y > n / 2 || b > n / 2)cout << "IMPOSSIBLE" << '\n';
		else {
			char one, two, three;
			if (r >= y&&r >= b) {
				one = 'R';
				if (y >= b) {
					two = 'Y';
					three = 'B';
				}
				else {
					two = 'B';
					three = 'Y';
				}
			}
			else if (y >= r&&y >= b) {
				one = 'Y';
				if (r >= b) {
					two = 'R';
					three = 'B';
				}
				else {
					two = 'B';
					three = 'R';
				}
			}
			else {
				one = 'B';
				if (r >= y) {
					two = 'R';
					three = 'Y';
				}
				else {
					two = 'Y';
					three = 'R';
				}
			}
			vi temp = { r,b,y };
			sort(all(temp));
			int bound = max(2 * temp[0] - 1,0);
			lop(i, 1, bound) {
				if (i % 2) {
					cout << three;
					temp[0]--;
				}
				else if (temp[0] + temp[1] > temp[2]) {
					cout << two;
					temp[1]--;
				}
				else {
					cout << one;
					temp[2]--;
				}
			}
			lop(i, bound+1, n) {
				if (i % 2) {
					cout << two;
					temp[1]--;
				}
				else {
					cout << one;
					temp[2]--;
				}
			}
			cout << '\n';
		}
	}
	return 0;
}