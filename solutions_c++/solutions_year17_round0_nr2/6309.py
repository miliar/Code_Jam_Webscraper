#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

void solve(int t)
{
    ll n, ans;
    cin >> n;
    vector<int> v;
    ll tmp = n;
    while (tmp > 0) {
        v.insert(v.begin(), tmp % 10);
        tmp /= 10;
    }
    int pos = 0;
    while (pos < v.size() - 1 && v[pos] <= v[pos + 1]) {
        pos++;
    }
    if (pos != v.size() - 1) {
        v[pos]--;
        while (pos > 0 && v[pos] < v[pos - 1]) {
            v[--pos]--;
        }
        pos++;
        for (; pos < v.size(); pos++) {
            v[pos] = 9;
        }
    }
    ans = 0;
    for (int d : v) {
        ans *= 10;
        ans += d;
    }
    cout << "Case #" << t << ": " << ans << endl;
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
