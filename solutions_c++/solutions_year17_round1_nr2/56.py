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
    assert(freopen("B.in", "r", stdin));
    freopen("B.out", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for (int tt = 0; tt < T; tt++) {
        printf("Case #%d: ", tt + 1);
        int n, m;
        scanf("%d%d", &n, &m);
        vector<int> r(n);
        for (int i = 0; i < n; i++)
            scanf("%d", &r[i]); 
        vector<vector<int>> b(n, vector<int> (m));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                scanf("%d", &b[i][j]);
            }
        }
        
        for (int i = 0; i < n; i++) {
            sort(all(b[i]));
        }


        int answer = 0;

        vector<int> cur(n, 0);
        for (int cnt = 1; ; cnt++) {
            bool fail = 0;
            for (int i = 0; i < n; i++)
                fail |= cur[i] == m;
            if (fail) break;
            for (int i = 0; i < n; i++) {
                for (; cur[i] < m && b[i][cur[i]] * 10 < cnt * r[i] * 9; cur[i]++);
            } 
            bool flag = 1;
            for (int i = 0; i < n; i++) {
                flag &= cur[i] < m && b[i][cur[i]] * 10 <= cnt * r[i] * 11;
            }
            if (flag) {
                for (int i = 0; i < n; i++) {
                    cur[i]++;
                }
                answer++;
                cnt--;
            }
        }
        
        cout << answer << endl;
    }
    
    
#ifdef HOME 
    epr("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
#endif
    return 0;
}

