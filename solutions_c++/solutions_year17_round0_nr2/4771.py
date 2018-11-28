#include <bits/stdc++.h>

#define F first
#define S second
#define prev azaza
#define mp make_pair
#define pb push_back

using namespace std;
typedef long long ll;
typedef long double ld;

const int max_n = 1, inf = 1000111222;

bool is_tidy(ll n) {
    vector<int> v;
    while(n) {
        v.pb(n % 10);
        n /= 10;
    }
    for (int i = 0; i < v.size() - 1; ++i) {
        if (v[i] < v[i + 1]) return false;
    }
    return true;
}

ll solve_dumb(string s)
{
    ll mn = 1;
    ll n = 0;
    for (int i = s.size() - 1; i >= 0; --i) {
        n += mn * (s[i] - '0');
        mn *= 10;
    }
    while(true) {
        if (is_tidy(n)) return n;
        --n;
    }
}

string solve(string s)
{
    string ans = "";
    for (int i = 0; i < s.size() - 1; ++i) {
        if (s[i] > s[i + 1]) {
            s[i]--;
            int j;
            for (j = i; j > 0; --j) {
                if (s[j - 1] <= s[j]) break;
                s[j - 1]--;
            }
            j++;
            for (; j < s.size(); ++j) {
                s[j] = '9';
            }
            break;
        }
    }
    bool isnon0 = false;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] != '0') {
            isnon0 = true;
        }
        if (s[i] == '0' && !isnon0) continue;
        ans += s[i];
    }
    return ans;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    ll n;
    cin >> T;
    string s;
    for (int I = 1; I <= T; ++I) {
        cin >> s;
        cout << "Case #" << I << ": " << solve(s) << endl;
    }
    return 0;
}


