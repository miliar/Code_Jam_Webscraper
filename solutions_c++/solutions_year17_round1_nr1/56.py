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



int main(){
#ifdef HOME 
    assert(freopen("A.in", "r", stdin));
    freopen("A.out", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for (int tt = 0; tt < T; tt++) {
        int n, m;
        scanf("%d%d", &n, &m);
        //db2(n, m);
        vector<string> s(n);
        for (int i = 0; i < n; i++) {
            cin >> s[i];
        }
        printf("Case #%d: ", tt + 1);
        cout << endl;
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (s[i][j] == '?')
                    s[i][j] = s[i][j - 1];
            }
            for (int j = m - 2; j >= 0; j--) {
                if (s[i][j] == '?')
                    s[i][j] = s[i][j + 1];
            }
        }
        for (int j = 0; j < m; j++) {
            for (int i = 1; i < n; i++) {
                if (s[i][j] == '?')
                    s[i][j] = s[i - 1][j];
            }
            for (int i = n - 2; i >= 0; i--) {
                if (s[i][j] == '?')
                    s[i][j] = s[i + 1][j];
            }
        }
        for (int i = 0; i < n; i++)
            cout << s[i] << endl;



    }
    
    
#ifdef HOME 
    epr("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
#endif
    return 0;
}

