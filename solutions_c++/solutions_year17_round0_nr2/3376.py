#include <bits/stdc++.h>
#define MAX_N 100100
using namespace std;

#define ll long long
#define ull unsigned long long
#define ii pair<int,int>
#define iii pair<ii, int>

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define ep emplace_back
#define sz(a) (int) a.size()
#define cl(a) a.clear()

#define vi vector<int>
#define vii vector<ii>

#define LOWBIT(x) ( (x) & -(x) )

#define FOR(x,a,b) for (int x=a;x<=b;x++)
#define FOD(x,a,b) for (int x=a;x>=b;x--)
#define REP(x,a,b) for (int x=a;x<b;x++)
#define RED(x,a,b) for (int x=a;x>b;x--)

const int MAX = 1e5 + 10;
const int MAXN = 1e4 + 10;
const int MOD = 1e9 + 7;
const int inf = 1e9;
const double pi = acos(-1.0);
const double eps = 1e-6;

int dx[] = {0 , -1 , 0 , 1};
int dy[] = {1 , 0 , -1 , 0};

int test;
string s;

int main() {
	ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);

    cin >> test; int t = test;

    while (test--) {
        cout << "Case #" << t - test << ": ";
        cin >> s;
        int l = s.size();

        int p = -1;

        REP(i , 1 , l)
            if (s[i] < s[i - 1]) {
                p = i - 1;
                break;
            }

        if (p == -1) {
            cout << s << endl;
            continue;
        }

        while (s[p] <= s[p - 1] && p) p--;

        if (p == 0 && s[0] <= '1') {
            FOR(i , 1 , l - 1) cout << '9';
            cout << endl;
            continue;
        }

        REP(i , 0 , p) cout << s[i];
        cout << (char) (s[p] - 1);
        REP(i , p + 1 , l) cout << '9';
        cout << endl;
    }

	return 0;
}
