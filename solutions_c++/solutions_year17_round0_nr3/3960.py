#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <queue>

using namespace std;

int N;
priority_queue<int> q;

int main(int argc, char const *argv[]) {
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    int T, kase = 1; cin>>T;
    while (T --) {
        int N, k;
        scanf("%d%d", &N, &k);
        while (!q.empty()) q.pop();
        q.push(N);
        for (int i = 0; i < k - 1; i ++) {
            int x = q.top(); q.pop();
            x --;
            if (x & 1) {
                int tmp = x / 2;
                q.push(tmp);
                q.push(x - tmp);
            }
            else {
                q.push(x / 2);
                q.push(x / 2);
            }
        }
        int x = q.top(); q.pop();
        x --;
        int a = x / 2, b = x - a;
        if (a < b) swap(a, b);
        printf("Case #%d: %d %d\n", kase ++, a, b);
    }
    return 0;
}