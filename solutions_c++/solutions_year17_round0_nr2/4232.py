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
		ll n;
		cin >> n;
		ll temp = n;
		vi digit;
		while (temp) {
			digit.pb(temp % 10);
			temp /= 10;
		}
		reverse(all(digit));
		vlop1(i, digit) {
			if (digit[i] < digit[i - 1]) {
				rlop(j, 0, i - 1) {
					if (!j) {
						digit[j]--;
						lop(k, j + 1, sz(digit)-1)digit[k] = 9;
						break;
					}
					else if (digit[j - 1] < digit[j]) {
						digit[j]--;
						lop(k, j + 1, sz(digit)-1)digit[k] = 9;
						break;
					}
				}
				break;
			}
		}
		ll result=0;
		vlop(i, digit) {
			result *= 10;
			result += digit[i];
		}
		cout << "Case #" << testcase << ": " << result<<endl;
	}
	return 0;
}