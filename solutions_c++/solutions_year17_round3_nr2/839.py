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
vii A, B;

int main() {
    ios::sync_with_stdio(false);
    int T;

    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        cin >> n >> m;
        A.resize(n);
        B.resize(m);
        cin >> A >> B;
        if (m == 2) {
            swap(A, B);
            swap(n, m);
        }

        int ans;
        if (n == 2) {
            sort(A.begin(), A.end());
            int a, b, c, d;
            a = A[0].second - A[0].first;
            b = A[1].first - A[0].second;
            c = A[1].second - A[1].first;
            d = 1440 - a - b - c;
            if (a + b + c <= 720 || c + d + a <= 720) {
                ans = 2;
            } else {
                ans = 4;
            }
        } else {
            ans = 2;
        }
        cout << "Case #" << cas << ": " << ans << endl;
    }
    return 0;
}
