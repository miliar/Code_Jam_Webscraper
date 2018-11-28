#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for (int i = (a); i < (b); i++)
#define pb push_back
typedef long long ll;

#define R 720

int T;

int c[2], cnt[2], dcnt[2];
int bt[2][234], bcnt[2];


struct r {
    int st, end, ty;
    r(int a, int b, int c) : st(a), end(b), ty(c) {}
    bool operator<(const r &oth) const {
        return st < oth.st;
    }
};
vector<r> rs;

void reset() {
 
    fo(i,0,2) {
        c[i] = cnt[i] = dcnt[i] = bcnt[i] = 0;
    }
    rs.clear();
}

int main() {
    scanf("%d", &T);
    fo(_,1,T+1) {
        printf("Case #%d: ", _);
        scanf("%d %d", c, c+1);
 
        int ans = 0;
        fo(i,0,2) {
            fo(j,0,c[i]) {
                int a, b; scanf("%d %d", &a, &b);
                rs.pb(r(a,b,i));
                cnt[i] += b-a;
            }
        }
        sort(rs.begin(), rs.end());
   
        int sum = 0; 
        int n = rs.size();
        fo(i,0,n) {
            int bk = (i-1+n)%n;
            int tm = (rs[i].st - rs[bk].end + 2*R)%(2*R); 
            if (rs[i].ty == rs[bk].ty) {
                int tt = rs[i].ty;
                cnt[tt] += tm;
                bt[tt][bcnt[tt]++] = tm;
            } else {
                ans++;
                sum += tm;
            }
        }
        fo(i,0,2) sort(bt[i], bt[i] + bcnt[i]);
        fo(i,0,2) while (cnt[i] > R) {
            ans += 2;
            cnt[i] -= bt[i][bcnt[i]-1];
            bcnt[i]--;
        } 
        printf("%d\n", ans);
        reset(); 
    }

    return 0;
}
