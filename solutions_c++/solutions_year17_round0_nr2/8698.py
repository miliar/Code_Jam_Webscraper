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
#define print(x) cout << (x) << endl
#define iterate(i, x) for (auto i = x.begin(); i != x.end(); i++)
#define max_ele(x) max_element(x.begin(), x.end())

int main (int argc, char *argv[]) {
    int t;
    cin >> t;
    for (int T = 1; T <= t; T++) {
        TESTCASE(T);
        string s;
        bool changed = false;
        int k = 0;
        cin >> s;

        for (int i = 0; i < s.length() - 1; i++) {
            if (s[i] > s[i + 1]) {
                s[k] = s[k] - 1;
                for (int j = k + 1; j < s.length(); j++)
                    s[j] = '9';
                changed = true;
                break;
            }

            if (s[i] != s[i + 1]) {
                k = i + 1;
            }
        }
        if (changed) {
            if (s[0] == '0')
                s.erase(s.begin());
            for (int i = 0; i < s.length() - 1 && s[i] == '0'; i++)
                s[i] = '9';
            print(s);
        }
        else {
            print(s);
        }
    }
    return 0;
}

