#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <functional>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <ctime>
#include <cmath>
// #include <tuple> // c++11
using namespace std;

#define st first
#define nd second
#define sz(col) ((int) col.size())
#define MEM(a,b) memset(a,b,sizeof(a))
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=a;i<=(b);++i)
#define getmid(l,r) ((l) + ((r) - (l)) / 2)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int MAX_N = 1024;

int dir[MAX_N];
int f[MAX_N];
int N, K;

int calc() {
    memset(f, 0, sizeof(f));
    int res = 0;
    int sum = 0;
    for (int i = 0; i + K <= N; i++)
    {
        if ((dir[i] + sum) % 2 != 0) {
            res++;
            f[i] = 1;
        }
        sum += f[i];
        if (i - K + 1 >= 0) 
        {
            sum -= f[i - K + 1];
        }
    }
    for (int i = N - K + 1; i < N; ++i)
    {
        if ((dir[i] + sum) % 2 != 0) {
            return -1;
        }
        if (i - K + 1 >= 0) {
            sum -= f[i- K + 1];
        }
    }
    return res;
}

int main() {
    freopen("A-large.bin", "r", stdin);
    freopen("A-large.sol", "w", stdout);
    int T; scanf("%d", &T);
    char s[MAX_N]; 
    for (int t = 1; t <= T; ++t)
    {
        scanf("%s%d", s, &K);
        N = strlen(s);
        for (int i = 0; i < N; ++i) dir[i] = (s[i] == '-' ? 1 : 0);
        int res = calc();
        if (res == -1) printf("Case #%d: IMPOSSIBLE\n", t);
        else printf("Case #%d: %d\n", t, res);
    }
}
