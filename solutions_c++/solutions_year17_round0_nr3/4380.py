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
	int t;
	cin >> t;
	lop(testcase, 1, t) {
		int n, k;
		cin >> n >> k;
		priority_queue<int> q;
		q.push(n);
		lop(i, 1, k-1) {
			int temp = q.top();
			q.pop();
			if (temp > 1) {
				if (temp == 2) q.push(1);
				else if (temp % 2) {
					q.push((temp - 1) / 2);
					q.push((temp - 1) / 2);
				}
				else {
					q.push((temp - 1) / 2);
					q.push((temp - 1) / 2 + 1);
				}
			}
		}
		int temp = q.top();
		if(temp%2)cout << "Case #" << testcase << ": "<<(temp-1)/2<<" "<<(temp-1)/2<<'\n';
		else cout << "Case #" << testcase << ": " << (temp - 1) / 2+1 << " " << (temp - 1) / 2 << '\n';
	}
	return 0;
}