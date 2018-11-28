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

int m;
string str;

int main() {
    initIO();
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        cin >> str >> m;
        int ans = 0;
        for (int i = str.size() - 1; i >= m - 1; i--) {
            if (str[i] == '-') {
                for (int j = i; j > i - m; j--) {
                    if (str[j] == '-')
                        str[j] = '+';
                    else
                        str[j] = '-';
                }
                ans++;
            }
            // cout << i << ": " << str << " " << ans << endl;
        }
        bool ok = true;
        for (int i = 0; i < str.size(); i++)
            if (str[i] == '-') {
                ok = false;
                break;
            }
        cout << "Case #" << cas << ": ";
        if (ok)
            cout << ans;
        else
            cout << "IMPOSSIBLE";
        cout << endl;
    }

    return 0;
}
