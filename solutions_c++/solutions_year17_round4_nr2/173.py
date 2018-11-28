#include <bits/stdc++.h>

using namespace std;


typedef long long ll;
typedef pair<int, int> pii;


const int N = 1010;
const int M = 100010;
const int inf = ~0U >> 1;
const int mod = 1e9 + 7;

int n, m, C;

struct SAP {
    struct node{int to, next; ll c;} e[M];
    int box[N], size, start, end, h[N], vh[N], tot;
    void clear(int n) {
        memset(box, -1, sizeof(box)), size = 0;
        tot = n;
        start = 1;
        end = tot;
    }
    void add(int from, int to, ll c){
        e[size].to = to;
        e[size].c = c;
        e[size].next = box[from];
        box[from] = size++;
        e[size].to = from;
        e[size].c = 0;
        e[size].next = box[to];
        box[to] = size++;
    }
    ll aug(int x, int c) {
        if(x == end) return c;
        int tem = h[x] + 1;
        ll l = c;
        for(int i = box[x]; ~i; i = e[i].next) if(e[i].c && h[e[i].to] + 1 == h[x]) {
                ll d = aug(e[i].to, min(e[i].c, l));
                e[i].c -= d, e[i ^ 1].c += d, l -= d;
                if(!l || h[start] == tot) return c - l;
            }
        for(int i = box[x]; ~i; i = e[i].next)
        if(e[i].c) tem = min(tem, h[e[i].to]);
        if(!--vh[h[x]]) h[start] = tot; else ++vh[h[x] = tem + 1];
        return c - l;
    }
    ll run() {
        ll s = 0;
        memset(h, 0, sizeof(h));
        memset(vh, 0, sizeof(vh));
        vh[0] = tot;
        while(h[start] < tot) s += aug(start, inf);
        return s;
    }
}sap;


int p[N], c[N];
void _main() {
    scanf("%d %d %d", &n, &C, &m);
    for (int i = 1; i <= m; ++i){
        scanf("%d %d", p + i, c + i);
        cnt_c[c[i]] ++;
        cnt_p[p[i]] ++;
    }

    int l = 0, r = 1e6, mid;
    for(int i = l; i < r; ++i) {
        mid = i;
        sap.clear(n);
        for(int i = 0; i < m; ++i) {
            sap.add(a[i], b[i], c[i]));
        }
        if(sap.run() >= x) l = mid;
        else r = mid;
    }
    for(int i = 1; i < N; ++i){
        ans += max(0, cnt_p[i] - l);
    }
    cout << l << " " << ans << endl;
    return 0;
}
int main() {
    int t, cas = 0;
    for (scanf("%d", &t); t--; ) {
        printf("Case #%d: ", ++cas);
        _main();
    }
    return 0;
}
