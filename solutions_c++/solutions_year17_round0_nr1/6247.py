#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <ctime>
#include <atomic>
#include <unordered_map>

using namespace std;

// bit manipulation
#define setBit(a, b) (a[b/32] |= (1 << (b%32)))
#define clearBit(a, b) (a[b/32] &= ~(1 << (b%32)))
#define testBit(a, b) (a[b/32] & (1 << (b%32)))

#define loop(i, n) for(auto i = 0; i < n; i++)
#define rloop(i, n) for(auto i = n - 1; i >= 0; i--)
#define mod(a, b) ((a % b + b) % b)
#define sortv(a) sort(a.begin(), a.end())
#define clean(a) sort(a.begin(), a.end()); a.erase(unique(a.begin(), a.end()), a.end())

#define startClock() const clock_t begin_time = clock()
#define endClock() std::cout << float( clock () - begin_time ) /  CLOCKS_PER_SEC << endl

#define file(a, b) ifstream cin(a); ofstream cout(b)
#define out(x) cout << x << endl;

typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<i64> vi;
typedef vector<st> vs;
typedef map<int, int> mii;
typedef map<st, int> msi;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

template<typename F, typename S>
ostream &operator<<(ostream &os, const pair<F, S> &p) {
    return os << "(" << p.first << ", " << p.second << ")";
}

template<typename T>
ostream &operator<<(ostream &os, const vector<T> &v) {
    os << "{";
    typename vector<T>::iterator it;
    for (it = v.begin(); it != v.end(); it++) {
        if (it != v.begin()) os << ", ";
        os << *it;
    }
    return os << "}";
}

template<typename T>
ostream &operator<<(ostream &os, const set<T> &v) {
    os << "[";
    typename set<T>::iterator it;
    for (it = v.begin(); it != v.end(); it++) {
        if (it != v.begin()) os << ", ";
        os << *it;
    }
    return os << "]";
}

template<typename F, typename S>
ostream &operator<<(ostream &os, const map<F, S> &v) {
    os << "[";
    typename map<F, S>::iterator it;
    for (it = v.begin(); it != v.end(); it++) {
        if (it != v.begin()) os << ", ";
        os << it->first << " = " << it->second;
    }
    return os << "]";
}

#define deb(x) cerr << #x << " = " << x << endl;

int main() {
    file("input.txt", "output.txt");
    i64 t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        st s;
        i64 k;
        cin >> s >> k;
        i64 ans = 0;
        for (int j = 0; j < s.size() - k + 1; j++) {
            if (s[j] == '-') {
                for (int m = 0; m < k; ++m) {
                    s[j + m] = s[j + m] == '-' ? '+' : '-';
                }
                ans++;
            }
        }
        for (int j = 0; j < s.size(); ++j) {
            if (s[j] == '-') {
                ans = -1;
                break;
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if (ans == -1) {
            out("IMPOSSIBLE");
        } else {
            out(ans);
        }
    }
    return 0;
}

//bool operator<(const ran &a, const ran &b) {
//    return a.p > b.p || (a.p == b.p && a.t < b.t);
//}