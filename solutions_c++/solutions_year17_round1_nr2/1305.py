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

void initIO() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
}

bool f(int g, int a, int i) {
    // a >= 0.9 * i * g;
    bool ret =  10ll * a >= 9ll * i * g;
    // cout << "g a i " << g << " " << a << " " << i << ": " << ret << endl;
    return ret;
}

bool f2(int g, int a, int i) {
    // a <= 1.1 * j * g;
    return 10ll * a <= 11ll * i * g;
}

ii get_range(int g, int a) {
    // a >= 0.9 * i * g;
    // find largest i
    // a <= 1.1 * j * g;
    // find smallest j
    int left, right;

    left = 0, right = 1e8;
    while (right - left > 1) {
        int mid = (left + right) / 2;
        if (f(g, a, mid)) {
            left = mid;
        } else {
            right = mid;
        }
    }
    int last = left;

    left = 0, right = 1e8;
    while (right - left > 1) {
        int mid = (left + right) / 2;
        if (f2(g, a, mid)) {
            right = mid;
        } else {
            left = mid;
        }
    }
    int first = right;
    return ii(first, last + 1);
}

int n, m;
vi G, A, B;
vii C, D;
int ans;

int main() {
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        cin >> n >> m;
        G.resize(n);
        cin >> G;
        // cout << "G: " << G << endl;
        if (n == 1) {
            A.resize(m);
            cin >> A;
            ans = 0;
            for (auto a: A) {
                auto r = get_range(G[0], a);
                // cout << a << ": " << r << endl;
                if (r.first < r.second)
                    ans++;
            }
        } else {
            A.resize(m);
            B.resize(m);
            C.resize(m);
            D.resize(m);
            cin >> A >> B;
            // cout << "A: " << A << endl;
            // cout << "B: " << B << endl;
            for (int i = 0; i < m; i++) {
                C[i] = get_range(G[0], A[i]);
                D[i] = get_range(G[1], B[i]);
                B[i] = i;
            }
            // cout << "C: " << C << endl;
            // cout << "D: " << D << endl;
            sort(B.begin(), B.end());
            ans = 0;
            do {
                int val = 0;
                for (int i = 0; i < m; i++) {
                    ii a = C[i];
                    ii b = D[B[i]];
                    // cout << "a: " << a << endl;
                    // cout << "b: " << b << endl;
                    int first = max(a.first, b.first);
                    int last = min(a.second, b.second);
                    // cout << "first last " << first << " " << last << endl;
                    if (first < last)
                        val++;
                }
                ans = max(ans, val);
            } while (next_permutation(B.begin(), B.end()));
        }
        cout << "Case #" << cas << ": " << ans << endl;
    }

    return 0;
}

