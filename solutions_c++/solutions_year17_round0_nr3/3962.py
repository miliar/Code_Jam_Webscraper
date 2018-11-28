#include <cstdio>
#include <queue>
using namespace std;
int T, n, k, res1, res2, buf;
int main() {
    freopen("csmall2.in", "r", stdin);
    freopen("csmall2.out", "w", stdout);
    scanf("%d", &T);
    for(int I = 1; I <= T; printf("Case #%d: %d %d\n", I++, res1, res2)) {
        scanf("%d %d", &n, &k);
        priority_queue<int> q;
        q.push(n);
        while(--k) {
            buf = q.top()-1;
            q.pop();
            q.push(buf/2+buf%2);
            q.push(buf/2);
        }
        buf = q.top()-1;
        res1 = buf/2 + buf%2;
        res2 = buf/2;
    }
    return 0;
}


