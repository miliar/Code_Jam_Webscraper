#include <iostream>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <iomanip>
#include <queue>
#include <utility>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<int, char> pci;

const int kInf = 1e9;

typedef tuple<int, int, int, int> Vertex;

int B, D, HD;

int Bfs(const Vertex& start) {
    map<Vertex, int> dist;
    queue<Vertex> q; q.push(start);
    dist[start] = 0;
    while (!q.empty()) {
        Vertex u = q.front();
        int u_dist = dist[u];
        int hd = get<0>(u), ad = get<1>(u), hk = get<2>(u), ak = get<3>(u);
        q.pop();
        if (hk <= 0) {
            return u_dist;
        }
        if (hd <= 0) {
            continue;
        }
        Vertex v;
        v = make_tuple(hd - ak, ad, hk - ad, ak);
        if (dist.count(v) == 0) {
            dist[v] = u_dist + 1;
            q.push(v);
        }
        v = make_tuple(hd - ak, ad + B, hk, ak);
        if (dist.count(v) == 0) {
            dist[v] = u_dist + 1;
            q.push(v);
        }
        v = make_tuple(HD - ak, ad, hk, ak);
        if (dist.count(v) == 0) {
            dist[v] = u_dist + 1;
            q.push(v);
        }
        v = make_tuple(hd - max(ak - D, 0), ad, hk, max(ak - D, 0));
        if (dist.count(v) == 0) {
            dist[v] = u_dist + 1;
            q.push(v);
        }
    }
    return kInf;
}

void Solve(int test_index) {
    int hd, ad, hk, ak;
    cin >> hd >> ad >> hk >> ak;
    cin >> B >> D;
    HD = hd;
    int res = Bfs(make_tuple(hd, ad, hk, ak));
    cout << "Case #" << test_index + 1 << ": ";
    if (res == kInf) {
        cout << "IMPOSSIBLE\n";
    } else {
        cout << res << '\n';
    }
    cerr << "Case #" << test_index + 1 << " done!" << "\n";
}

int main() {
    std::ios_base::sync_with_stdio(false);
    int tests_count;
    cin >> tests_count;
    for (int test_index = 0; test_index < tests_count; ++test_index) {
        Solve(test_index);
    }
    return 0;
}
