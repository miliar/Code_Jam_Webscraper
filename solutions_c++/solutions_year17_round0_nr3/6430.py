#include <bits/stdc++.h>

using namespace std;

const int INF = 0x3f3f3f3f;

int t, n, k;
int L[1111], R[1111];
int vis[1111];

struct A{
    int x, y, id;
    bool operator < (const A & b) const {
        if(x != b.x)
            return x < b.x;
        else if(x == b.x && y != b.y)
            return y < b.y;
        else if(x == b.x && y == b.y && id != b.id)
            return id > b.id;
    }
};

int f = 0;

int main() {
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    while(t--) {
        memset(vis, 0, sizeof vis);
        scanf("%d%d", &n, &k);
        for(int i = 1; i <= n; i++) {
            L[i] = i - 1;
            R[i] = n - i;
        }
        vis[0] = vis[n+1] = 1;
        A now;
        for(int i = 0; i < k; i++) {
            now = {0, 0, 0};
            for(int i = 1; i <= n; i++) {
                if(!vis[i])
                    now = max(now, A{min(L[i], R[i]), max(L[i], R[i]), i});
            }
            vis[now.id] = 1;
            int j;
            for(j = now.id - 1; j >= 0; j--) {
                R[j] = now.id - j - 1;
                if(vis[j])
                    break;
            }
            for(j = now.id + 1; j <= n + 1; j++) {
                L[j] = j - now.id - 1;
                if(vis[j])
                    break;
            }
        }
        printf("Case #%d: ", ++f);
        cout<<now.y<<" "<<now.x<<endl;
    }
    return 0;
}
