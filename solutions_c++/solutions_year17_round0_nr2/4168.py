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

long long n = 0;
long long m;
set<long long> S;

void backtrack(int cur) {
    if (cur)
        S.insert(m);
    if (cur == 18)
        return;

    if (cur == 0) {
        for (int i = 1; i <= 9; i++) {
            m = i;
            backtrack(cur + 1);
        }
    } else {
        int s = m % 10;
        for (int i = s; i <= 9; i++) {
            m = (m * 10) + i;
            backtrack(cur + 1);
            m /= 10;
        }
    }
}

int main() {
    initIO();
    int T;

    backtrack(0);
    /*
    cout << "s.size(): " << S.size() << endl;
    // cout << "S: " << S << endl;
    for (auto itr = prev(S.end()); distance(itr, S.end()) <= 100; itr = prev(itr)) {
        cout << *itr << endl;
    }
    */

    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        cin >> n;
        auto itr = lower_bound(S.begin(), S.end(), n);
        if (*itr > n) {
            itr = prev(itr);
        }
        cout << "Case #" << cas << ": " << *itr << endl;
    }
    return 0;
}
