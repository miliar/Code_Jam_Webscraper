#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef long double ld;
const double PI = acos(-1.);
const int MOD = 1000 * 1000 * 1000 + 7;

void getTest(vector<int> &conf, int &k) {
//    int len = rand() % 11 + 2;
//    k = rand() % (len + 1);
//    k = max(k, 2);
//    for (int i = 0; i < len; ++i) {
//        conf.emplace_back(rand() % 2);
//    }
    string s;
    cin >> s >> k;
    conf.resize(s.size());
    for (int i = 0; i < s.size(); ++i) {
        conf[i] = s[i] == '-' ? 0 : 1;
    }
    return;
}

void dfs(vector<int> &v, int k, map<vector<int>, int> &dp, int dist = 0) {
    dp[v] = dist;
    for (int i = 0; i < v.size() - k + 1; ++i) {
        vector<int> to = v;
        for (int j = 0; j < k; ++j) {
            to[i + j] ^= 1;
        }
        if (dp.find(to) == dp.end() || dp[to] > dist + 1) {
            dfs(to, k, dp, dist + 1);
        }
    }
    return;
}

int brute(vector<int> conf, int k) {
    map<vector<int>, int> visited;
    dfs(conf, k, visited);
    vector<int> want(conf.size(), 1);
    if (visited.find(want) != visited.end()) {
        return visited[want];
    }
    return -1;
}

///// & & &
int solve(vector<int> &conf, int k) {
    int res = 0;
    for (int i = 0; i < conf.size() - k + 1; ++i) {
        if (conf[i] == 1) continue;
        for (int j = 0; j < k; ++j) {
            conf[i + j] ^= 1;
        }
        ++res;
    }
    for (int i = 0; i < conf.size(); ++i) {
        if (conf[i] == 0) return -1;
    }
    return res;
}

int main() {
    //srand(time(nullptr));
    freopen("/home/york_io/Documents/Code/contest/in.txt", "r", stdin);
    //freopen("/home/york_io/Documents/Code/contest/out.txt", "r", stdin);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        vector<int> conf;
        int k;
        getTest(conf, k);
        ll res = solve(conf, k);
        if (res == -1) {
            cout << "case #" << t << ": ";
            cout << "IMPOSSIBLE\n";
            continue;
        }
        cout << "case #" << t << ": " << res << endl;
//        if (solve(conf, k) != brute(conf, k)) {
//            for (int i = 0; i < conf.size(); ++i) {
//                cout << conf[i] << " ";
//            }
//            cout << endl << k << endl;
//            cout << brute(conf, k) << " " << solve(conf, k);
//            return 0;
//        }
//        for (int i = 0; i < conf.size(); ++i) {
//            cout << conf[i] << " ";
//        }
//        cout << endl << k << endl;
//        cout << "OK " << t << endl;
    }
    return 0;
}