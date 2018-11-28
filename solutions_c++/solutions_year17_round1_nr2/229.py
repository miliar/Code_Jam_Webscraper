#include <bits/stdc++.h>
using namespace std;

struct Enode{
    int y, c, next;
} e[2005 * 2005 * 3];

int n, m, tot, head[2005], now[2005], h[2005], vh[2005], augc, found, flow;

void addedge(int x, int y, int c){
    e[++tot].y = y; e[tot].c = c; e[tot].next = head[x]; head[x] = tot;
    e[++tot].y = x; e[tot].c = 0; e[tot].next = head[y]; head[y] = tot;
}

void Aug(int x, int st, int ed, int n){
    int p = now[x], minh = n - 1, augco = augc;
    if (x == ed){
        found = 1;
        flow += augc;
        return;
    }
    while (p != -1){
        if (e[p].c > 0 && h[e[p].y] + 1 == h[x]){
            augc = min(augc, e[p].c);
            Aug(e[p].y, st, ed, n);
            if (h[st] >= n) return;
            if (found) break;
            augc = augco;
        }
        p = e[p].next;
    }
    if (found){
        e[p].c -= augc;
        e[p ^ 1].c += augc;
    }else{
        p = head[x];
        while (p != -1){
            if (e[p].c > 0 && h[e[p].y] < minh){
                minh = h[e[p].y];
                now[x] = p;
            }
            p = e[p].next;
        }
        vh[h[x]] --;
        if (!vh[h[x]]) h[st] = n;
        h[x] = minh + 1;
        vh[h[x]] ++;
    }
}
void Maxflow(int st, int ed, int n){
    flow = 0;
    memset(h, 0, sizeof(h));
    memset(vh, 0, sizeof(vh));
    vh[0] = n;
    while (h[st] < n){
        found = 0;
        augc = 1 << 30;
        Aug(st, st, ed, n);
    }
}

int num_of_gram[55];
int l[55][55], r[55][55];

int getr(int x, int y) {
    int l = 1, r = (int)(y * 1.2), ans = -1;
    while (l <= r) {
        int mid = l + r >> 1;
        if (1ll * mid * x * 9 <= y * 10) {
            ans = mid;
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return ans;
}

int getl(int x, int y) {
    int l = 1, r = (int)(y * 1.2), ans = -1;
    while (l <= r) {
        int mid = l + r >> 1;
        if (1ll * mid * x * 11 >= y * 10) {
            ans = mid;
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    return ans;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int CAS, n, p, x;
    cin >> CAS;
    for (int cas = 1; cas <= CAS; cas++) {
        scanf("%d%d", &n, &p);
        for (int i = 0; i < n; i++) {
            scanf("%d", &num_of_gram[i]);
        }
        tot = -1; memset(head, -1, sizeof(head));
        int st = 0, ed = n * p * 2 + 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                addedge(i * p + j + 1, (i + n) * p + j + 1, 1);
                scanf("%d", &x);
                l[i][j] = getl(num_of_gram[i], x);

                r[i][j] = getr(num_of_gram[i], x);
            }
            if (!i) {
                for (int j = 0; j < p; j++) if (l[i][j] <= r[i][j]){
                    addedge(st, j + 1 + n * p, 1);
                }
            } else {
                for (int j = 0; j < p; j++) if (l[i][j] <= r[i][j]){
                    for (int k = 0; k < p; k++) if (l[i - 1][k] <= r[i - 1][k]) {
                        if (!((l[i][j] > r[i - 1][k]) || (r[i][j] < l[i - 1][k]))) {
                            addedge((i - 1 + n) * p + k + 1, i * p + j + 1, 1);
                        }
                    }
                }
            }
            if (i == n - 1) {
                for (int j = 0; j < p; j++) if (l[i][j] <= r[i][j]){
                    addedge((i + n) * p + j + 1, ed, 1);
                }
            }
        }
        memcpy(now, head, sizeof(head));
        Maxflow(st, ed, n * p * 2 + 2);
        printf("Case #%d: %d\n", cas, flow);
    }
}
