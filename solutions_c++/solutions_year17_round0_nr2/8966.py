#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <climits>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>

#define FORT for(int t=1;t<=T;t++)
#define REP(x,s,n) for(int x=s; x<n; x++)
#define EPSILON (1E-6)
#define CODEJAM 0
#define MAXN 131073
#define sz(s) (s).size()
#define pb(s) push_back((s))
#define all(s) (s).begin(),(s).end()

using namespace std;

typedef long int LI;
typedef long long LL;
typedef long double LD;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef map<int,int> mii;

bool CompareDouble(const LD &, const LD &);

int main() {
    freopen("qualB-large.in", "r+", stdin);
    freopen("outputB-large.txt", "w+", stdout);
    int T;
    cin >> T;
    FORT {
		string s;
		cin >> s;
		int l = s.size() - 1;
		int startnine = 100;
		for (int i = l; i>0; i--) {
			if (s[i] - '0' < s[i-1] - '0') {
				s[i] = '9';
				s[i-1] = char(s[i-1] - 1);
				startnine = i;
			}
		}
		printf("Case #%d: ", t);
		for (int i = 0; i < s.size(); i++) {
			if (i >= startnine) cout << '9';
			else if (s[i] == '0') continue;
			else cout << s[i];
		}
		cout << endl;
    }
    return 0;
}

bool CompareDouble(const LD &a, const LD &b) {
    return fabs(a - b) < EPSILON;
}
