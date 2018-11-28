#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;

#define INF 1000000000 // 1 billion, safer than 2B for Floyd Warshall’s
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define REP(i, n) for(int i=0;i<(n);i++)
#define FOR(i, a, b) for(int i=(a);i<=(b);i++)
#define FORD(i, a, b) for(int i=(a);i>=(b);i--)

inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

int main() {
    ios::sync_with_stdio(false);
    int T;
    string N;
    cin >> T;
    int cas = 1;
    while (T-- > 0) {
    	cin >> N;
    	for(int k = 0; k < N.length(); ++k) {
	    	for(int i = 0; i < N.length() - 1; ++i) {
	    		if (N[i] > N[i + 1]) {
	    			N[i] = N[i] - 1;
	    			for(int j = i + 1; j < N.length(); ++j) {
	    				N[j] = '9';
	    			}
	    			break;
	    		}
	    	}
	    }
    	int i = 0;
    	while (N[i] == '0') ++i;
    	cout << "Case #" << cas++ <<": ";
    	for(;i < N.length(); ++i) {
    		cout << N[i];
    	}
    	cout << endl;



    }
    return 0;
}