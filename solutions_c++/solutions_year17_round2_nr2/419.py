//84104971101048411497 - Can you guess what does this mean?
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef complex<double> point;
#define mapii map<int, int>
#define debug(a) cout << #a << ": " << a << endl
#define debuga1(a, l, r) fto(i, l, r) cout << a[i] << " "; cout << endl
#define fdto(i,  r, l) for(int i = (r); i >= (l); --i)
#define fto(i, l, r) for(int i = (l); i <= (r); ++i)
#define forit(it, var) for(__typeof(var.begin()) it = var.begin(); it != var.end(); it++)
#define forrit(rit, var) for(__typeof(var.rbegin()) rit = var.rbegin(); rit != var.rend(); rit++)
#define ii pair<int, int>
#define iii pair<int, ii>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define X real()
#define Y imag()
#define maxN 1005
#define oo 1000000007
#define NIL 0

const double PI = acos(-1.0);

double fRand(double fMin, double fMax)
{
    double f = (double)rand() / RAND_MAX;
    return fMin + f * (fMax - fMin);
}

template <class T>
T min(T a, T b, T c) {
    return min(a, min(b, c));
}

template <class T>
T max(T a, T b, T c) {
    return max(a, max(b, c));
}

int nTest, n, r, o, y, g, b, v;
bool canAdj[256][256];

bool Check(string s) {
    fto(i, 0, n-1)
        if (!canAdj[s[i]][s[(i+1)%n]]) return false;
    return true;
}

string Solve() {
    string ans;
    if (r > 0) ans += 'R';
    else if (y > 0) ans += 'Y';
    else if (b > 0) ans += 'B';
//    printf("%d %d %d\n", r, y, b);
    fto(i, 0, n-1) {
//        debug(ans);
        if (ans[i] == 'B') {
            --b;
            if (b < 0) return "IMPOSSIBLE";
            if (i < n-1) ans += (r > y) ? 'R' : 'Y';
        } else if (ans[i] == 'R') {
            --r;
            if (r < 0) return "IMPOSSIBLE";
            if (i < n-1) ans += (b > y) ? 'B' : 'Y';
        } else {
            --y;
            if (y < 0) return "IMPOSSIBLE";
            if (i < n-1) ans += (r > b) ? 'R' : 'B';
        }
    }
    //debug(ans);
    if (Check(ans)) return ans;
    swap(ans[n-2], ans[n-1]);
    if (Check(ans)) return ans;
    return "IMPOSSIBLE";
}

int main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    canAdj['R']['B'] = canAdj['R']['Y'] = canAdj['R']['G'] = true;
    canAdj['Y']['R'] = canAdj['Y']['B'] = canAdj['Y']['V'] = true;
    canAdj['B']['R'] = canAdj['B']['Y'] = canAdj['B']['O'] = true;
    canAdj['O']['B'] = true;
    canAdj['G']['R'] = true;
    canAdj['V']['Y'] = true;

    scanf("%d", &nTest);
    fto(iTest, 1, nTest) {
        scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
        printf("Case #%d: %s\n", iTest, Solve().c_str());
    }

    return 0;
}
