#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

struct node{
    int len, a, b;
    bool operator < (const node &b) const {
        if (len != b.len) return len<b.len;
        else if (a!=b.a) return a>b.a;
    }
    bool operator > (const node &b) const {
        return !((*this)<b);
    }
};

int main() {
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-small-2-attempt0.out", "w", stdout);
    int T, cnt = 0;
    scanf("%d", &T);
    while(T--) {
        priority_queue<node>q;
        int n, k;
        scanf("%d%d", &n, &k);
        q.push(node{n+1, 0, n+1});
        for(int i = 1; i <= k; i++) {
            int a = q.top().a, b = q.top().b;
            q.pop();
            int p = (a + b) / 2;
            if(i == k) printf("Case #%d: %d %d\n", ++cnt, max(p-a-1, b-p-1), min(p-a-1, b-p-1));
            q.push(node{p-a, a, p}), q.push(node{b-p, p, b});
        }
    }
}
