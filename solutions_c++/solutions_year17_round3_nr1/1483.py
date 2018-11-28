#include <bits/stdc++.h>
#define prt(k) cerr<<#k" = "<<k<<endl
#define pln(k) cout<<#k" = "<<k<<endl;
typedef long long LL;
const int INF = 0x3f3f3f3f;
void read(int &re) { scanf("%d", &re); }
using namespace std;
const int MAXN = 2344;
const double PI = acos(-1.0);
int N, K;
//int R[MAXN], H[MAXN];
struct P
{
    int R,H;
    bool operator < (P b) const
    {
        return 1LL*R*H > 1LL*b.R*b.H;
    }
}p[MAXN];;

int main()
{
    int re, ca = 1; cin>>re;
    while (re--) {
        cin>>N>>K;
        for (int i=0;i<N;i++) {
            int R,H;
            cin>>R>>H;
            p[i] = (P){R,H};
        }
        sort(p,p+N);
        double ans = 0;
        for (int i=0;i<N;i++) {
            double now =  1.0*p[i].R*p[i].R + 2.0*p[i].R*p[i].H; //prt(now);
            int cnt = 0;
            for (int j=0;cnt<K-1&&j<N;j++) if (p[j].R<=p[i].R && i-j) {
                now += 2 * 1.0*p[j].R*p[j].H;
                cnt++;
              //  prt(j);prt(now);
              //  if (++cnt == K-1) break;
            }
           // prt(now );
           // puts("");
            ans = max(ans, now*PI);
        }
        printf("Case #%d: %.10f\n", ca++, ans);
   //     for (int i=0;i<R;i++) cout<<a[i]<<endl;
    }
    return 0;
}
