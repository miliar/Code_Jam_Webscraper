#include <bits/stdc++.h>

#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define forn(i, n) for(int i=0;i<(n);++i)
#define clr(ar, val) memset(ar, val, sizeof(ar))

using namespace std;

typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef pair<ld, ld> point;

const int MAXN = 2e5 + 200;
const int INF = int(1e9) + 7;
const long long LINF = 1ll * INF * INF;
const int md = int(1e9) + 7;
const ld eps = 1e-9;
const ld PI = 3.1415926535897932384626433832795l;

int it, test;
long long n, k;
std::priority_queue<long long> q;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> test;
    for (it = 1; it <= test; it++) {
        while (!q.empty()) q.pop();
        cin >> n >> k;
        q.push(n);
        long long curVal = 0;
        for (int i = 0; i < k; i++) {
            curVal = q.top();
            q.pop();

            if (curVal & 1) {
                q.push(curVal / 2);
            } else {
                q.push(curVal / 2 - 1);
            }

            q.push(curVal / 2);
        }

        long long ansMax, ansMin;
        if (curVal & 1) {
            ansMax = ansMin = curVal / 2;
        } else {
            ansMax = curVal / 2;
            ansMin = ansMax - 1;
        }
        cout << "Case #" << it << ": " << ansMax << " " << ansMin << endl;
    }
    return 0;
}
