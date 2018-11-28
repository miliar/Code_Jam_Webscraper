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
    freopen("qualA-small.in", "r+", stdin);
    freopen("outputA-small.txt", "w+", stdout);
    int T;
    cin >> T;
    FORT {
		string s;
		int k;
		cin >> s;
		cin >> k;
		int res = 0;
		int l = s.size();
		for (int i = 0; i <= l-k; i++) {
			if (s[i] == '-') {
				for (int j = 0; j < k && i+k <= l; j++) s[i+j] = (s[i+j] == '-') ? '+' : '-';
				res++;
			}
		}
		//cout << endl << s<<endl;
		int flag = 0;
		for (int i = 0; i < l; i++) {
			if (s[i] == '-') flag = 1;
		}
		printf("Case #%d: ", t);
		if (flag) cout << "IMPOSSIBLE"; 
		else cout << res;
		cout << endl;
    }
    return 0;
}

bool CompareDouble(const LD &a, const LD &b) {
    return fabs(a - b) < EPSILON;
}
