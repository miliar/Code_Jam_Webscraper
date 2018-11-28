#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;

int T, N, R, O, Y, G, B, V;

vector<int> solve(int c, int b, int a) {
    vector<int> res;
    if (a > b + c) return res;
    for (int i = 0; i < c + b - a; ++i) {
        res.push_back(2), res.push_back(1), res.push_back(0);
    }
    for (int i = 0; i < b - (c + b - a); ++i) {
        res.push_back(2), res.push_back(1);
    }
    for (int i = 0; i < c - (c + b - a); ++i) {
        res.push_back(2), res.push_back(0);
    }
}

int main() {
    ios::sync_with_stdio(false);
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N >> R >> O >> Y >> G >> B >> V;
        cout << "Case #" << t << ": ";
        if (R < G) {
            cout << "IMPOSSIBLE\n"; continue;
        }
        if (Y < V) {
            cout << "IMPOSSIBLE\n"; continue;
        }
        if (B < O) {
            cout << "IMPOSSIBLE\n"; continue;
        }
        if (R && R == G) {
            if (R + G == N) {
                for (int i = 0; i < N / 2; ++i) {
                    cout << "RG";
                }
                cout << '\n'; continue;
            }
            cout << "IMPOSSIBLE\n"; continue;
        }
        if (Y && Y == V) {
            if (Y + V == N) {
                for (int i = 0; i < N / 2; ++i) {
                    cout << "YV";
                }
                cout << '\n'; continue;
            }
            cout << "IMPOSSIBLE\n"; continue;
        }
        if (B && B == O) {
            if (B + O == N) {
                for (int i = 0; i < N / 2; ++i) {
                    cout << "BO";
                }
                cout << '\n'; continue;
            }
            cout << "IMPOSSIBLE\n"; continue;
        }
        R -= G, Y -= V, B -= O;
        vector<ii> a;
        a.push_back(ii(R, 0)), a.push_back(ii(Y, 1)), a.push_back(ii(B, 2));
        sort(a.begin(), a.end());
        vector<int> v = solve(a[0].first, a[1].first, a[2].first);
        if (v.size() == 0) {
            cout << "IMPOSSIBLE\n"; continue;
        }
        for (int i = 0; i < v.size(); ++i) {
            int tmp = a[v[i]].second;
            if (tmp == 0) {
                if (!G) { cout << 'R'; continue; }
                for (int j = 0; j < G; ++j) cout << "RG";
                cout << 'R'; G = 0; continue;
            }
            else if (tmp == 1) {
                if (!V) { cout << 'Y'; continue; }
                for (int j = 0; j < V; ++j) cout << "YV";
                cout << 'Y'; V = 0; continue;
            }
            else {
                if (!O) { cout << 'B'; continue; }
                for (int j = 0; j < O; ++j) cout << "BO";
                cout << 'B'; O = 0; continue;
            }
        }
        cout << '\n';
    }
}
