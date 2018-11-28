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

#define maxn 1010
int n, m;
vii A;
double B[maxn][maxn];

int main() {
    ios::sync_with_stdio(false);
    int T;
    
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        cin >> n >> m;
        A.resize(n);
        cin >> A;
        sort(A.begin(), A.end(), greater<ii>());
        // cout << "A: " << A << endl;
        memset(B, 0, sizeof(B));
        for (int i = 1; i <= n; i++) {
            double r = A[i-1].first;
            double h = A[i-1].second;
            for (int j = 1; j <= m; j++) {
                for (int k = 0; k < i; k++) {
                    if (j == 1) {
                        B[i][j] = max(B[i][j], B[k][j-1] + r * r * M_PI + 2 * r * M_PI * h);
                    } else {
                        B[i][j] = max(B[i][j], B[k][j-1] + 2 * r * M_PI *h);
                    }
                }
            }
        }
        /*
        cout << "B:" << endl;
        for (int i = 0; i <= n; i++) {
            cout << i << ": ";
            for (int j = 0; j <= m; j++) {
                cout << B[i][j] << " ";
            }
            cout << endl;
        }
        */
        double ans = 0;
        for (int i = 1; i <= n; i++)
            ans = max(ans, B[i][m]);
        cout << "Case #" << cas << ": " << fixed << setprecision(9) << ans << endl;
    }
    return 0;
}
