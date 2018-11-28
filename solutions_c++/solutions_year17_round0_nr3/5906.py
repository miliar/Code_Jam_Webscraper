#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <ctime>
#include <cassert>

using namespace std;

#define REP(i, n) for (int i = 0; i < (n); ++i)
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;

const int INF = 0x7fffffff;
int T, N, K;

int main() {
//#ifdef __AiR_H
//    freopen("C-small-1-attempt1.in", "r", stdin);
//    freopen("C-small-1-attempt1.out", "w", stdout);
//#endif // __AiR_H
    int Case = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%d %d", &N, &K);
        priority_queue<int> q;
        q.push(N);
        int Max = N, Min = N, t;
        while (K--) {
            t = q.top(); q.pop();
            if (t % 2) { Min = t / 2; }
            else { Min = (t - 1) / 2; }
            Max = t / 2;
            if (t % 2) { q.push(t / 2); q.push(t / 2); }
            else { q.push(t / 2); q.push((t - 1) / 2); }
        }
        printf("Case #%d: %d %d\n", ++Case, Max, Min);
    }
    return 0;
}
