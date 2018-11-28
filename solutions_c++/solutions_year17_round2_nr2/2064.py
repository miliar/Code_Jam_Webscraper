#include <bits/stdc++.h>
#define MOD (1000000007)

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef vector<string> vs;

template<typename T1, typename T2>
pair<T1, T2> operator+(pair<T1, T2> a, pair<T1, T2> b) {
    return make_pair(a.first + b.first, a.second + b.second);
}

template<typename T1, typename T2>
pair<T1, T2> operator-(pair<T1, T2> a, pair<T1, T2> b) {
    return make_pair(a.first - b.first, a.second - b.second);
}

template<typename T1, typename T2>
ostream& operator<<(ostream& out, pair<T1, T2> p) {
    out << p.first << " " << p.second;
    return out;
}

template<typename T1, typename T2>
istream& operator>>(istream& in, pair<T1, T2>& p) {
    in >> p.first >> p.second;
    return in;
}

template<typename T>
ostream& operator<<(ostream& out, vector<T> v) {
    for (auto a: v)
        out << a << " ";

    return out;
}

template<typename T>
istream& operator>>(istream& in, vector<T>& v) {
    for (auto &a: v)
        in >> a;

    return in;
}

template<typename T>
ostream& operator<<(ostream& out, multiset<T> S) {
    for (auto a: S)
        out << a << " ";

    return out;
}

template<typename T>
ostream& operator<<(ostream& out, set<T> S) {
    for (auto a: S)
        out << a << " ";

    return out;
}

template<typename T1, typename T2>
ostream& operator<<(ostream& out, map<T1,T2>& M) {
    for (auto m: M)
        out << "[" << m.first << "]=" << m.second << " " ; 

    return out;
}

int n;
vi A;
vector<pair<int, char>> C;
vvi B;

void output() {
    for (int i = 0; i < B.size(); i++) {
        cout << C[0].second;
        for (int j = 0; j < B[i].size(); j++) {
            cout << C[B[i][j]].second;
        }
    }
    cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    int T;

    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        A.resize(6);
        cin >> n >> A;
        C.resize(3);
        C[0] = make_pair(A[0], 'R');
        C[1] = make_pair(A[2], 'Y');
        C[2] = make_pair(A[4], 'B');
        for (int i = 1; i < 3; i++)
            if (C[i].first > C[0].first)
                swap(C[i], C[0]);
        if (C[2].first > C[1].first)
            swap(C[2], C[1]);
        for (int i = 0; i < 3; i++)
            A[i] = C[i].first;
        A.resize(3);
        // cout << "A: " << A << endl;
        bool ok = true;
        if (ok) {
            int m = A[0];
            B.resize(m);
            for (auto &b: B)
                b.clear();
            for (int i = 0; i < A[1] - A[2]; i++) {
                B[i].push_back(1);
            }
            /*
            for (int i = 0; i < B.size(); i++)
                cout << "B " << i << ": " << B[i] << endl;
            */
            int i = A[1] - A[2];
            while (A[2] && i < m) {
                if (i + 1 <= m - 1) {
                    B[i].push_back(1);
                    B[i+1].push_back(2);
                    i += 2;
                } else {
                    B[i].push_back(1);
                    B[i].push_back(2);
                }
                A[2]--;
            }
            while (A[2]) {
                if (B[0].back() == 1) {
                    B[0].push_back(2);
                    B[0].push_back(1);
                } else {
                    B[0].push_back(1);
                    B[0].push_back(2);
                }
                A[2]--;
            }
            for (int i = 0; i < m; i++) {
                if (B[i].empty()) {
                    ok = false;
                    break;
                }
            }
            /*
            for (int i = 0; i < B.size(); i++)
                cout << "B" << i << ": " << B[i] << endl;
            */
        }
        cout << "Case #" << cas << ": ";
        if (ok) {
            output();
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
