#include <iostream>
#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

typedef pair<int, char> PP;

int N, R, O, Y, G, B, V;

void solve()
{
    vector<PP> v;
    v.push_back({R, 'R'});
    v.push_back({Y, 'Y'});
    v.push_back({B, 'B'});
    sort(v.rbegin(), v.rend());

    if (v[0].first > v[1].first + v[2].first) {
        cout << "IMPOSSIBLE";
        return;
    }

    int a[1000] = {};
    int b[1000] = {};
    int c[1000] = {};
    int cnt = v[0].first;

    for (int i = 0; i < v[0].first; i++) a[i] = 1;
    for (int i = 0; i < v[1].first; i++) b[i] = 1;
    for (int i = 0; i < v[2].first; i++) c[cnt - 1 - i] = 1;

    for (int i = 0; i < cnt; i++) {
        if (a[i]) cout << v[0].second;
        if (b[i]) cout << v[1].second;
        if (c[i]) cout << v[2].second;
    }
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N >> R >> O >> Y >> G >> B >> V;
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }
}
