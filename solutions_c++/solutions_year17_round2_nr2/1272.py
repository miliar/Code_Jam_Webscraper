#include <bits/stdc++.h>
using namespace std;

#define TASK ""

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef long double ld;
typedef pair<int, int> pairi;
typedef pair<ll, ll> pairll;
typedef pair<ld, ld> pairld;

#define all(v) v.begin(),v.end()
#define forn(s, n) for (int i = s; i < n; i++)
#define mp make_pair
#define pb push_back
#define sz size
#define EPS 1e-7

const int INF = INT_MAX / 2, NINF = INT_MIN / 2;
const ld PI = acos(-1.0);

void prepareIO () {
}

void debout() {
}

template <typename Head, typename... Tail>
void debout(Head H, Tail... T) {
#ifdef _DEBUG
    cerr << H << ' ';
    debout(T...);
#endif
}

class Timer {
public:
    double begin;
    Timer () : begin(clock()) {}
    ~Timer() {
        fprintf(stderr, "%.6lf\n", (clock() - begin + .0) / CLOCKS_PER_SEC);
    }
} timer_;

void solve1();

int main() {
    prepareIO();
    solve1();
    return 0;
}

string small2(int n, int r, int y) {
    string s = "";
    while (r > 0 && y > 0) {
        s += "RY";
        r--;
        y--;
    }

    while (r > 0) {
        s += 'R';
        r--;
    }

    while (y > 0) {
        s += 'Y';
        y--;
    }

    return s;
}

int calcCol(string& s) {
    int res = 0;
    for (int i = 0; i < s.size(); i++) {
        char nextCh;
        if (i + 1 == s.size())
            nextCh = s[0];
        else
            nextCh = s[i + 1];
        if (s[i] == nextCh)
            res++;
    }

    return res;
}

string small(int n, int r, int y, int b) {
    auto s = small2(n - b, r, y);
    int col = calcCol(s);
    if (col > b)
        return "IMPOSSIBLE";
    string ans = "";
    for (int i = 0; i < s.size(); i++) {
        ans += s[i];
        char nextCh;
        if (i + 1 == s.size())
            nextCh = s[0];
        else
            nextCh = s[i + 1];
        if (nextCh == s[i]) {
            ans += 'B';
            b--;
        }
    }

    string ans2 = "";
    for (int i = 0; i < ans.size(); i++) {
        char nextCh;
        ans2 += ans[i];
        if (i + 1 == ans.size())
            nextCh = ans[0];
        else
            nextCh = ans[i + 1];
        if (ans[i] == 'B' || nextCh == 'B' || b == 0) {
            continue;
        }

        ans2 += 'B';
        b--;
    }

    if (b > 0)
        return "IMPOSSIBLE";

    return ans2;
}

void solve(int t) {
    int n;
    int arr[6] = {};
    cin >> n;
    for (int i = 0; i < 6; i++)
        cin >> arr[i];

    auto s = small(n, arr[0], arr[2], arr[4]);
    cout << s << "\n";
}

void solve1() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve(i + 1);
    }
}

