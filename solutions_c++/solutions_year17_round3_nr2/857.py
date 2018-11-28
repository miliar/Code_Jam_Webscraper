#include <bits/stdc++.h>
#define base 1000000007LL
#define ll long long
#define X first
#define Y second
#define pb push_back
#define Scan(a) scanf("%I64d", &a)
#define CLR(a) memset(a,0,sizeof(a))
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORE(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)

using namespace std;

typedef pair<int, int> II;
typedef vector<II> vi;

struct data {
    int x, y;
} a[10], b[10];

bool operator< (data a, data b) {
    return a.y < b.y;
}

int n, m;

int main()
{
    ios::sync_with_stdio(0);
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    FOR(o,1,t) {
        cout << "Case #" << o << ": ";
        cin >> n >> m;
        FOR(i,1,n) cin >> a[i].x >> a[i].y;
        FOR(i,1,m) cin >> b[i].x >> b[i].y;
        sort(a+1, a+n+1);
        sort(b+1, b+m+1);
        if (n == 2) {
            if (1440-a[2].y + a[1].x >= 720) cout << 2 << endl;
            else if (a[2].x - a[1].y >= 720) cout << 2 << endl;
            else cout << 4 << endl;
        }
        else if (m == 2) {
            if (1440-b[2].y + b[1].x >= 720) cout << 2 << endl;
            else if (b[2].x - b[1].y >= 720) cout << 2 << endl;
            else cout << 4 << endl;
        }
        else {
            cout << 2 << endl;
        }
    }
    return 0;
}
