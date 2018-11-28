#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

void flip(string& s, int k, int from)
{
    if (from + k > s.size()) {
        return;
    }
    for (int i = from; i < from + k; i++) {
        s[i] = (s[i] == '+') ? '-' : '+';
    }
}

int count(string& s, int k, int from)
{
    int i = 0;
    for (int i = k; i < min<size_t>(from + k, s.size()); i++) {
        if (s[from + i] != '-') {
            break;
        }
    }
    return i + 1;
}

void solve(int t)
{
    string s;
    ll k, ans = 0;
    cin >> s >> k;
    int pos = 0;
    bool imp = false;
    while (pos < s.size()) {
        if (s[pos] == '+') {
            pos++;
        } else {
            // cout << s.size() << " " << pos << endl;
            if (pos > s.size() - k) {
                imp = true;
                break;
            }
            flip(s, k, pos);
            ans++;
            // cout << pos << endl;
            // cout << s << endl;
        }
    }
    cout << "Case #" << t << ": ";
    if (imp) {
        cout << "IMPOSSIBLE";
    } else {
        cout << ans;
    }
    cout << endl;
}

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        solve(i + 1);
    }
    return 0;
}
