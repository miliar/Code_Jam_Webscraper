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

int bits[32];
int len;

void solve()
{
    int i;
    i = 0;
    while (i < len - 1 && bits[i + 1] >= bits[i]) ++i;
    if (i == len - 1) return;
    while (i > 0 && bits[i-1] == bits[i]) --i;
    bits[i] -= 1;
    for (int j = i + 1; j < len; ++j) bits[j] = 9;
}


int main()
{
    freopen("B-large.bin", "r", stdin);
    freopen("B-large.sol", "w", stdout);
    int T; scanf("%d", &T);
    char s[32];
    for (int t = 1; t <= T; ++t)
    {
        scanf("%s", s); 
        len = strlen(s);
        memset(bits, 0, sizeof(bits));
        for (int i = 0; i < len; ++i)
        {
            bits[i] = s[i] - '0';
        }
        solve();
        printf("Case #%d: ", t);
        int i = 0;
        for (; i < len && bits[i] == 0; ++i);
        for (; i < len; ++i) {
            printf("%d", bits[i]);
        }
        printf("\n");
    }
}
