#include <bits/stdc++.h>

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

template<typename T>
ostream& operator<<(ostream& out, unordered_set<T> S) {
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

int n, m;
int U;
vi A;
set<ii> S;

int main() {
    ios::sync_with_stdio(false);
    int T;

    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        cin >> n >> m;
        {
            int a, b; char c;
            cin >> a >> c >> b;
            U = a * 10000 + b;
        }
        A.resize(n);
        for (int i = 0; i < n; i++) {
            int a, b;
            char ch;
            cin >> a >> ch >> b;
            A[i] = a * 10000 + b;
        }
        // cout << "A: " << A << endl;
        S.clear();
        for (int i = 0; i < n; i++) {
            S.insert(ii(A[i],i));
        }
        while (U--) {
            auto s = S.begin()->second;
            S.erase(S.begin());
            A[s]++;
            S.insert(ii(A[s],s));
        }

        double ans = 1;
        for (int i = 0; i < n; i++) {
            double val = A[i] / 10000.0;
            ans *= val;
        }
        cout << "Case #" << cas << ": " << fixed << setprecision(6) << ans << endl;
    }
    return 0;
}
