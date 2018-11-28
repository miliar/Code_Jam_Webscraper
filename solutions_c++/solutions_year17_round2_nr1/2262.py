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

int d, n;
vi pos, speed;

int main() {
    ios::sync_with_stdio(false);
    int T;
    double ans = 0.0;

    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        cin >> d >> n;
        pos.resize(n);
        speed.resize(n);
        for (int i = 0; i < n; i++) {
            cin >> pos[i] >> speed[i];
        }
        ans = numeric_limits<double>::max();
        for (int i = 0; i < n; i++) {
            double val = 1.0 * d * speed[i] / (d - pos[i]);
            ans = min(ans, val);
        }

        // cout << "pos: " << pos << endl;
        // cout << "speed: " << speed << endl;
        cout << "Case #" << cas << ": " << fixed << setprecision(6) << ans << endl;
    }
    return 0;
}
