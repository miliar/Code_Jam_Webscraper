#include <bits/stdc++.h>
using namespace std;
#define prt(k) cout<<#k" = "<<k<<"   ";
#define pln(k) cout<<#k" = "<<k<<endl;
typedef long long LL;
const int MAXN = 8701000 ;
const int INF = 0x3f3f3f3f;
typedef pair<LL, LL> P;
const P null = P(-1,-1);
//int a[MAXN];
LL  n , K;

void M(P &a, P &b) /// Merge
{
    if (a.first == b.first) {
        a.second += b.second;
        LL t = b.second;
        b.second = 0;
   //     return P(a.first, a.second + t);
    }
//    return null;
}
P L(P a)
{
    return P(a.first / 2, a.second);
}
P R(P a)
{
    return P((a.first - 1) / 2, a.second);
}
LL BFS(LL n, LL K)
{

    if (K==1) return n;
 //   if (K==2) return n / 2;
 //   if (K==3) return (n - 1) / 2;
    K -= 1;
    P a, b; LL cnt = 2;
    a = P(n/2, 1); b = P((n-1)/2, 1);
    while (true) {
        if (K <= cnt) {
            if (K <= a.second) return a.first;
            else return b.first;
        }
        K -= cnt;
        P p[4], aa, bb;
        p[0] = L(a); p[1] = R(a); p[2] = L(b); p[3] = R(b);
        int i;
        for (i=1;i<4;i++) M(p[0], p[i]);
        a = p[0];
        for (i=1;i<4;i++) if (p[i].first - p[0].first) break;
        if (i == 4) i = 1;
        for (int j=i+1;j<4;j++) M(p[i], p[j]);
        b = p[i];
        if (a.first < b.first) swap(a, b);

        cnt = cnt * 2;
    }

}
int main()
{
//    freopen("asfd", "w", stdout);
    int re ,ca = 1;
    cin >> re;
    while (re--)
    {
        cin >>n >> K;
        LL u = BFS(n, K);
        printf("Case #%d: %lld %lld\n", ca++, u/2, (u-1)/2);
    }
}
