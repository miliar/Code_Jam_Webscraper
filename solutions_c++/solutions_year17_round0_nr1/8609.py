#include <bits/stdc++.h>
using namespace std;

typedef vector<bool> vb;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vii> graph;
typedef long long ll;
typedef unsigned long long ull;

#define FOR(i, x, y) for (auto i = x; i < y; i++)
#define FOR_R(i, x, y) for (auto i = x; i >= y; i--)
#define TESTCASE(T) cout << "Case #" << T << ": "
#define print(x) cout << x << endl
#define iterate(i, x) for (auto i = x.begin(); i != x.end(); i++)
#define max_ele(x) max_element(x.begin(), x.end())

    //cout << "string " << s << " Cur index " << index << endl;
#define MAX 9999999

int k;

int rec_solve(string s, int index) {
    bool allDone = true;
    for (char c : s)
        if (c == '-')
            allDone = false;
    if (allDone)
        return 0;

    if (s.length() < index + k) {
        return MAX;
    }

    string invert_s = s;
    for (int i = index; i < index + k; i++)
        invert_s[i] = (invert_s[i] == '+') ? '-' : '+';
    return min(rec_solve(invert_s, index + 1) + 1, rec_solve(s, index + 1));
}

int main (int argc, char *argv[]) {
    int t;
    cin >> t;
    for (int T = 1; T <= t; T++) {
        TESTCASE(T);
        string s;
        cin >> s >> k;
        int res = rec_solve(s, 0);
        if (res == MAX)
            cout << "IMPOSSIBLE\n";
        else
            print(res);
    }
    return 0;
}

