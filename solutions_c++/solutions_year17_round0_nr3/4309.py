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

void initIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}


long long n, k;
map<long long, long long, greater<long long>> M;

void output() {
    cout << "M: ";
    for (auto m: M) {
        cout << "[" << m.first << ", " << m.second << "] ";
    }
    cout << endl;
}

int main() {
    initIO();
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        cin >> n >> k;
        // cout << n << " " << k << endl;
        M.clear();
        M[n] = 1;
        long long cnt = 0;
        long long s;
        long long ans1, ans2;
        // output();
        while (cnt < k) {
            s = M.begin()->first;
            if (s % 2) {
                if (s >= 3)
                    M[s/2] += M[s] * 2;
            } else {
                if (s == 2) {
                    M[s-1] += M[s];
                } else if (s >= 4) {
                    M[s/2] += M[s];
                    M[s/2-1] += M[s];
                }
            }
            cnt += M[s];
            M.erase(M.begin());
            // cout << "s: " << s << ", cnt: " << cnt << endl;
            // output();
        }
        if (s % 2)
            ans1 = ans2 = s / 2;
        else
            ans1 = s / 2, ans2 = s / 2 - 1;
        cout << "Case #" << cas << ": " << ans1 << " " << ans2 << endl;
    }

    return 0;
}
