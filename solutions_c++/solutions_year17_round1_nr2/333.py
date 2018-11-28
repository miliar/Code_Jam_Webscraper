// In the name of god
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <ctime>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <bitset>
#define sqr(a) ((a)*(a))
#define all(a) (a).begin(), (a).end()
using namespace std;
 
template <typename T>
T next_int() {
    T x = 0, p = 1;
    char ch;
    do { ch = getchar(); } while(ch <= ' ');
    if(ch == '-') {
        p = -1;
        ch = getchar();
    }
    while(ch >= '0' && ch <= '9') {
        x = x * 10 + (ch - '0');
        ch = getchar();
    }
    return p * x;
}
 
string next_token() {
    char ch;
    string ans = "";
    do { ch = getchar(); } while(ch <= ' ');
    while(ch > ' ') {
        ans += ch;
        ch = getchar();
    }
    return ans;
}
 
const long long INF = (long long)1e18;
const int INFINT = (int)1e9 + 227 + 1;
const int MAXN = (int)1e6 + 227 + 1;    
const int MOD = (int)1e9 + 7;
const long double EPS = 1e-9;

long long bin_pow(long long a, long long b) {
    if(!b) return 1;
    long long ans = bin_pow(a, b / 2);
    ans = ans * ans % MOD;
    if(b % 2) ans = ans * a % MOD;
    return ans;
}

pair<long long, long long> get(long long a, long long b) {
    long long l = 1;
    long long r = 1e9;

    // for(int i = 1; i <= 12; i++) {
    //     bool ok = 1;

    //     ok &= (a * 100 >= b * i * 90);
    //     // ok &= (a * 100 <= b * i * 110);

    //     cout << ok;
    // }
    // puts("");

    while(r - l > 1) {
        long long c = (l + r) / 2;
        if(a * 100 >= b * c * 90)
            l = c;
        else
            r = c;
    }

    long long le = -1;
    if(a * 100 >= b * r * 90)
        le = r;
    else
    if(a * 100 >= b * l * 90)
        le = l;

    l = 1;
    r = 1e9;

    while(r - l > 1) {
        long long c = (l + r) / 2;
        if(a * 100 <= b * c * 110)
            r = c;
        else
            l = c;
    }

    long long re = -1;
    if(a * 100 <= b * l * 110)
        re = l;
    else
    if(a * 100 <= b * r * 110)
        re = r;

    if(le == -1 || re == -1 || le < re) 
        return make_pair(-1, -1);

    return make_pair(re, le);
}

int main() {
    freopen(".in", "r", stdin);
    freopen("t.out", "w", stdout);

    int test; cin >> test;
    for(int num = 1; num <= test; num++) {
        cout << "Case #" << num << ": "; 
    
        int n, m; cin >> n >> m;

        vector<int> b(n);
        for(int i = 0; i < n; i++)
            b[i] = next_int<int>();

        vector<vector<int> > a(n);
        for(int i = 0; i < n; i++) {
            a[i].resize(m);
            for(int j = 0; j < m; j++)
                a[i][j] = next_int<int>();
        }

        map<int, vector<pair<bool, pair<int, int> > > > q;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                int l = get(a[i][j], b[i]).first;
                int r = get(a[i][j], b[i]).second;

                if(l == -1) continue;

                q[l].push_back(make_pair(1, make_pair(i, r)));
                q[r + 1].push_back(make_pair(0, make_pair(i, r)));
            }
        }

        vector<multiset<int> > e(n);
        map<pair<int, int>, int> t;
        int ans = 0;
        for(map<int, vector<pair<bool, pair<int, int> > > > :: iterator i = q.begin(); i != q.end(); i++) {
            vector<pair<bool, pair<int, int> > > w = i -> second;

            sort(all(w));

            for(int i = 0; i < w.size(); i++) {
                if(w[i].first) 
                    e[w[i].second.first].insert(w[i].second.second);
                else {
                    if(t[w[i].second])
                        t[w[i].second]--;
                    else
                        e[w[i].second.first].erase(e[w[i].second.first].lower_bound(w[i].second.second));
                }
            }

            int it = INFINT;
            for(int i = 0; i < n; i++)
                it = min(it, (int)e[i].size());

            ans += it;

            while(it--) {
                for(int i = 0; i < n; i++) {
                    pair<int, int> f = make_pair(i, *e[i].begin());
                    e[i].erase(e[i].begin());
                    t[f]++;
                }
            }
        }

        cout << ans << "\n";
    }
}
