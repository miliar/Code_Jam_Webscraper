#include <iostream>
#include <queue>

using namespace std;

struct S {
    int l, r;
};
S s[1001];
bool used[1001];
S solve2(int n, int k) {
    memset(used, false, 1001);
    S ans;
    
    for (int i = 0; i < n; i++) {
        s[i].l = i;
        s[i].r = n - i - 1;
    }
    while (k--) {
        ans.l = -1;
        ans.r = -1;
        int idx = 0;
        for (int i = 0; i <  n; i++) {
            if (used[i]) continue;
            int mi = min(s[i].l, s[i].r);
            int ma = max(s[i].l, s[i].r);
            if (mi > ans.l) {
                idx = i;
                ans.l = mi;
                ans.r = ma;
            } else if (mi == ans.l && ma > ans.r) {
                idx = i;
                ans.r = ma;
                ans.l = mi;
            }
        }
        used[idx] = true;
        for (int i = idx + 1; i < n; i++) {
            s[i].l = i - idx - 1;
            if (used[i]) break;
        }
        for (int i = idx - 1; i >= 0; i--) {
            s[i].r = idx - i - 1;
            if (used[i]) break;
        }
    }
    return ans;
}

int solve(int n, int k) {
    priority_queue<int> q;
    q.push(n);
    for (int i = 1; i < k; i++) {
        int t = q.top();
        q.pop();
        if (t > 1) {
            int l = t / 2;
            q.push(l);
            if (t & 1) q.push(l);
            else if (l - 1 > 0) q.push(l - 1);
        }
    }
    int ans = q.top();
    // while(!q.empty()) q.pop();
    return ans;
}

int main(int argc, const char * argv[]) {
    int T;
    scanf("%d", &T);
    for (int caseno = 0; caseno < T; caseno++) {
        int n,k;
        scanf("%d %d", &n, &k);
        int t = solve(n, k);
        int l = t / 2;
        printf("Case #%d: %d %d\n", caseno + 1, l, (t & 1) ? l : l - 1);
    }
    return 0;
}
