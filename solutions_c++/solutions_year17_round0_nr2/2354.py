#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <random>
#include <functional>

using namespace std;

#define F first
#define S second
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 
#define db3(x, y, z) cerr << "(" << #x << ", " << #y << ", " << #z << ") = (" << x << ", " << y << ", " << z << ")\n"
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)a.size()
#define pw(n) (1ll << (n))

#define equal equalll
#define less lesss
const int N = -1;
const long long INF = 1e9 + 19;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef double dbl;


bool check(vector<int> b) {
    for (int i = 0; i + 1 < (int)b.size(); i++)
        if (b[i] < b[i + 1])
            return 0;
    return 1;
}

int main() {
#ifdef HOME 
    assert(freopen("in", "r", stdin));
    freopen("B.out", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for (int tt = 0; tt < T; tt++) {
        printf("Case #%d: ", tt + 1);
        ll x;
        cin >> x;
        vector<int> tmp;
        ll xx = x;
        for (; x > 0; x /= 10)
            tmp.pb(x % 10);
        
        bool ok = 1;
        for (int i = 1; i < (int)tmp.size(); i++) {
            ok &= tmp[i - 1] >= tmp[i];
        }
        if (ok) {
            cout << xx << endl; 
            continue;
        }
        //db(tmp.size());

        for (int i = 0; i < (int)tmp.size(); i++) {
            if (i + 1 == (int)tmp.size() || tmp[i] > tmp[i + 1]) {
                //db(i);
                auto b = tmp;
                b[i]--;
                for (int j = 0; j < i; j++)
                    b[j] = 9;

                if (check(b)) {
                    ll res = 0;
                    for (int j = (int)b.size() - 1; j >= 0; j--) {
                        res = res * 10 + b[j];
                    }
                    cout << res << endl;
                    assert(res < xx);
                    break;
                }
            }
        }




    }

    
    
#ifdef HOME 
    epr("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
#endif
    return 0;
}

