#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair <int, int> pii;
typedef vector<int> vi;

#define mp make_pair
#define pb push_back

#define FOR(i, a, b) for (int i=a; i<b; i++)
#define F0R(i, a) for (int i=0; i<a; i++)
 
#define f first
#define s second
#define lb lower_bound
#define ub upper_bound
#define endl "\n"
 
const int MOD = 1000000007;
double PI = 4*atan(1);

int R,C;
char grid[25][25];

void fill(int row) {
    char x = '?';
    F0R(i,C) {
        if (grid[row][i] == '?') grid[row][i] = x;
        else x = grid[row][i];
    }
    for (int i = C-1; i >= 0; --i) {
        if (grid[row][i] == '?') grid[row][i] = x;
        else x = grid[row][i];
    }
}

void solve() {
    char temp[25];
    F0R(i,25) temp[i] = '?';
    F0R(i,R) {
        bool x = 0;
        F0R(j,C) if (grid[i][j] != '?') x = 1;
        if (x == 0) {
            F0R(j,C) grid[i][j] = temp[j];
        } else {
            F0R(j,C) temp[j] = grid[i][j];
        }
    }
    for (int i = R-1; i >= 0; --i) {
        bool x = 0;
        F0R(j,C) if (grid[i][j] != '?') x = 1;
        if (x == 0) {
            F0R(j,C) grid[i][j] = temp[j];
        } else {
            F0R(j,C) temp[j] = grid[i][j];
        }
    }
    F0R(i,R) fill(i);
}

int main() {
	int T; cin >> T;
	F0R(i,T) {
		cout << "Case #" << (i+1) << ":\n";
		cin >> R >> C;
		F0R(j,R) F0R(k,C) cin >> grid[j][k];
		solve();
		F0R(j,R) {
		    F0R(k,C) cout << grid[j][k];
		    cout << "\n";
		}
	}
}