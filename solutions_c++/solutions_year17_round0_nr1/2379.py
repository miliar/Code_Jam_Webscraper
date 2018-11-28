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


char change(char ch) {
    if (ch == '+') return '-';
    if (ch == '-') return '+';
    assert(false);
}

int main(){
#ifdef HOME 
    assert(freopen("in", "r", stdin));
    freopen("D.out", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for (int tt = 0; tt < T; tt++) {
        printf("Case #%d: ", tt + 1);
        string s;
        cin >> s;
        int k;
        cin >> k;
        int answer = 0;
        int n = s.size();
        for (int i = 0; i + k <= n; i++) {
            if (s[i] == '-') {
                answer++;
                for (int j = 0; j < k; j++)
                    s[i + j] = change(s[i + j]);
            }
        }
        bool ok = 1;
        for (int i = 0; i < n; i++)
            ok &= s[i] == '+';
        if (ok) {
            printf("%d\n", answer);
        }
        else {
            puts("IMPOSSIBLE");
        }




    }

    
    
#ifdef HOME 
    epr("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
#endif
    return 0;
}

