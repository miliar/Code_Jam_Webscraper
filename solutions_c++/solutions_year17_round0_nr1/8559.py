#include <set>
#include <map>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <ctime>
#include <deque>
#include <bitset>
#include <cctype>
#include <utility>

#define ULL unsigned long long
#define LL long long
#define FOR(i,a,b) for(int i = (a); i <= (int)(b); i++)
#define FO(i,a,b) for(int i = (a); i < (int)(b); i++)
#define FORD(i,a,b) for(int i= (a); i >= (int)(b); i--)
#define FOD(i,a,b) for(int i= (a); i > (int)(b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define SET(a,c) memset(a, c, sizeof(a))
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(), (a).end()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
#define eps 1e-5
#define infi 1e9
#define PI 2*acos(0.0)
#define debug(k,F,n) FOR(i,1,n){FOR(j,1,n) cout << setw(k) << F[i][j]  ; cout << endl;}
using namespace std;

typedef pair<int,int>II;
typedef pair<int,II>PII;
typedef vector<int> VI;
typedef vector<II> VII;
typedef set<int> SI;
typedef map<string,int> MSI;
typedef map<int,int> MII;

template<class T> T gcd(T a, T b) {
    T r;
    while (b != 0) {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}
template<class T> T lcm(T a, T b) {
    return a / gcd(a, b) * b;
}
template<class T> T sqr(T x) {
    return x * x;
}
template<class T> T cube(T x) {
    return x * x * x;
}
template<class T> int getbit(T s, int i) {
    return (s >> i) & 1;
}
template<class T> T onbit(T s, int i) {
    return s | (T(1) << i);
}
template<class T> T offbit(T s, int i) {
    return s & (~(T(1) << i));
}
template<class T> T togglebit(T s, int i) {
    return s ^ (T(1) << i);
}
template<class T> int cntbit(T s) {
    return s == 0 ? 0 : cntbit(s >> 1) + (s & 1);
}
#define maxn  305
#define MOD 1000000005

int test, k;
string s;

int main()
{
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);

    cin >> test;
    FOR (n_test, 1, test) {
        cout << "Case #" << n_test << ": ";
        cin >> s;
        cin >> k;
        int start_bit = (1 << k) - 1;
        vector<int> changes;
        changes.push_back(start_bit);
        FO (i, 1, s.length() - k + 1) {
            start_bit = start_bit << 1;
            changes.push_back(start_bit);
        }
//        FO (i, 0, sz(changes)) {
//            cout << changes[i] << " ";
//        }

        int n = 0;
        char first_bit = s[0];
        int destination = 0;
        if (first_bit == '+') {
            destination = (1<<s.length()) - 1;
        }
//        cout << destination;
        FO (i, 0, s.length()) {
            if (s[i] == first_bit) {
                n = (n << 1) + 1;
            }   else {
                n = n << 1;
            }
        }

        queue<pair<int, int> > q;
        set<int> pushed;
        q.push(mp(n,0));

        bool printed = false;
        while (!q.empty()) {
            pair<int, int> entry = q.front();
            q.pop();
            if (entry.first == destination) {
                cout << entry.second;
                printed = true;
                break;
            }
            int step = entry.second;
//            int state = entry.first;

            FO (i, 0, sz(changes)) {
                int change_way = changes[i];
                int original = entry.first;
//                int tmp = 0;
                FOR (j, 0, s.length()) {
                    int bit = getbit(change_way, j);
                    if (bit == 1) {
                        original = togglebit(original, j);
                    }
                }
                if (pushed.find(original) == pushed.end()) {
                    pushed.insert(original);
                    q.push(mp(original, step + 1));
                }
            }
        }
        if (!printed) {
            cout << "IMPOSSIBLE";
        }

        cout << endl;

    }

    return 0;
}