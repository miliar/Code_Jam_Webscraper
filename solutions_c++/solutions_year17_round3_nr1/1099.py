#include <bits/stdc++.h>
#define file
using namespace std;

const double pi = acos(-1.0);
int f = 0;
int t;
int n, k;
struct A{
    double r, h;
    double s1, s2;
    bool used;
    void gets() {
        s1 = 2*pi*r*h + pi*r*r;
        s2 = 2*pi*r*h;
    }
} pan[1100];

bool cmp1(A a, A b) {
    return a.s1 > b.s1;
}

bool cmp2(A a, A b) {
    return a.s2 > b.s2;
}

int main() {
    #ifdef file
    freopen("A-large.in", "r", stdin);
    freopen("1out.txt", "w", stdout);
    #endif // file
    scanf("%d", &t);
    while(t--) {
        scanf("%d%d", &n, &k);
        for(int i = 0; i < n; i++)
            scanf("%lf%lf", &pan[i].r, &pan[i].h), pan[i].used = 0, pan[i].gets();
        double res = 0;
        for(int i = 0; i < n; i++) {
            double ans = pan[i].s1;
            vector<A> G;
            for(int j = 0; j < n; j++)
                if(i == j) continue;
                else G.push_back(pan[j]);
            sort(G.begin(), G.end(), cmp2);
            int cnt = k - 1;
            for(int j = 0; j < G.size() && cnt; j++) {
                if(G[j].r <= pan[i].r)
                    ans += G[j].s2, cnt--;
                if(cnt == 0) break;
            }
            if(cnt == 0)
                res = max(res, ans);
        }
        printf("Case #%d: %.10f\n", ++f, res);
    }
    return 0;
}
