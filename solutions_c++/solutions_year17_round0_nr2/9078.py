#include <bits/stdc++.h>
#include <cstdlib>

using namespace std;

#define all(v)                  v.begin(), v.end()
#define db(x)                   cerr << #x << " = " << (x) << "\n"
#define fend(x)                 ((x) & ((x)+1)) - 1
#define fenu(x)                 (x) | ((x)+1)
#define forn(i, n)              for (int i = 0; i < (int)n; ++i)
#define forr(i, b, e)           for (int i = b; i < (int)e; ++i)
#define ft                      first
#define len(s)                  s.length()
#define mp                      std::make_pair
#define pob                     pop_back
#define pof                     pop_front
#define pub                     push_back
#define puf                     push_front
#define sc                      second

typedef double dbl;
typedef long double ldbl;
typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;

const long long MILLER_RABIN = 3215031751;
const long double PI = acos(-1);

#if __cplusplus >= 201103L

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <cstdlib>

struct config_io {
    config_io() {
        cin.tie(nullptr);
        cout.tie(nullptr);
        ios_base::sync_with_stdio(false);
    }
} cnf_io;

struct config_rand {
    config_rand() {
        srand(chrono::duration_cast<chrono::nanoseconds>(
                chrono::high_resolution_clock::now().time_since_epoch()).count());
    }
} cnf_rand;

namespace std {
    template<>
    struct hash<pair<int, int> > {
        size_t operator()(const pair<int, int> &x) const {
            return (x.first * 71ull + x.second) % ((int) 1e9 + 7);
        }
    };

    template<>
    struct hash<vector<int>> {
        size_t operator()(const vector<int> &v) const {
            size_t hsh = 0;
            for (int i = 0; i < v.size(); ++i) {
                hsh = (hsh * 71ull + v[i]) % (int) (1e9 + 7);
            }
            return hsh;
        }
    };
}

template<class T>
using ordered_set = __gnu_pbds::tree<T, __gnu_pbds::null_type, less<T>, __gnu_pbds::rb_tree_tag, __gnu_pbds::tree_order_statistics_node_update>;
//ordered_set<int>  s;
//s.insert(3);
//cout << s.order_of_key(2) << endl; // the number of elements in the s less than 2
//cout << *s.find_by_order(0) << endl; // print the 0-th smallest number in s(0-based)

// __builtin_popcount(x) - Returns the number of 1-bits in x.
// __builtin_parity(x) - Returns the parity of x, i.e. the number of 1-bits in x modulo 2.
// __builtin_ffs(x) - Returns one plus the index of the least significant 1-bit of x, or if x is zero, returns zero.
// __builtin_clz(x) - Returns the number of leading 0-bits in x, starting at the most significant bit position. If x is 0, the result is undefined.
// __builtin_ctz(x) - Returns the number of trailing 0-bits in x, starting at the least significant bit position. If x is 0, the result is undefined.

//inline string tobin(long long x) { bitset<63>(x).to_string(); }

template<class T>
void trace(T collection) {
    for (auto elem : collection) { cout << elem << " "; }
    cout << endl;
}

#endif

struct solution {

    struct pr {
#define __TYPE__ ll
        __TYPE__ x, y;

        pr() {}

        pr(__TYPE__ _x, __TYPE__ _y) : x(_x), y(_y) {}

        friend __TYPE__ cross(const pr &p1, const pr &p2) {
            return p1.x * p2.y - p1.y * p2.x;
        }

        friend __TYPE__ dot(const pr &p1, const pr &p2) {
            return p1.x * p2.x + p1.y * p2.y;
        }

        friend bool operator<(const pr &p1, const pr &p2) {
            return p1.x < p2.x || (p1.x == p2.x && p1.y < p2.y);
        }

        friend bool operator==(const pr &p1, const pr &p2) {
            return p1.x == p2.x && p1.y == p2.y;
        }

        struct hasher {
            size_t operator()(const pr &p) const {
                return p.x * 1234567ULL + p.y;
            }
        };
    };

    bool isGood(string num) {
        forr(i, 1, num.length()) {
            if (num[i] < num[i - 1]) {
                return false;
            }
        }
        return true;
    }

    void solve(int test) {
        ll num;
        cin >> num;
        string s = to_string(num);
        if (isGood(s)) {
            cout << "Case #" << test << ": " << s << endl;
        } else {
            int n = s.length();
            forr(i, 1, n) {
                if (s[i] < s[i - 1]) {
                    int from = i;
                    if (i - 1 > 0 && s[i - 1] == s[i - 2]) from = i - 1;
                    while (from > 0 && s[from] == s[from - 1]) from--;
                    if (!from) from++;
                    ll rem = atoll(s.substr(from).c_str());
                    //db(s), db(rem);
                    num -= rem + 1;
                    if (!isGood(to_string(num))) cerr << "jofjeojroejfoejfof" << endl;
                    cout << "Case #" << test << ": " << num << endl;
                    return;
                }
            }
        }
    }
};

int main() {
#ifdef HOME
    freopen("home.in", "r", stdin);
    freopen("home.out", "w", stdout);
#endif

    //    ifstream is("home.out");
    //    int x;
    //    vector<int> v;
    //    while(is >> x) {
    //        v.push_back(x);
    //    }
    //    ifstream is2("hangar.out.3");
    //    int ptr = 0;
    //    while(is2 >> x) {
    //        if(x != v[ptr]) {
    //            cout << ptr << " " << x << " " << v[ptr] << endl;
    //        }
    //        ptr++;
    //    }

    int tests = 1;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        solution sol;
        sol.solve(test);
        //        cin.clear();
        //        cin.seekg(0, ios::beg);
    }

#ifdef HOME
    cerr << "\n\nTime: " << clock() / (double) CLOCKS_PER_SEC << endl;
#endif
    return 0;
}