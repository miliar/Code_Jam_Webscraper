#include <bits/stdc++.h>
#define prt(k) cerr<<#k" = "<<k<<endl
#define pln(k) cout<<#k" = "<<k<<endl;
typedef long long LL;
const int INF = 0x3f3f3f3f;
void read(int &re) { scanf("%d", &re); }
using namespace std;
typedef pair<int,int> Z;
int N, P;
int R[342];
LL Q[66][66];
bool used[88][87];
bool OK[88];
LL dfs(int i, int t)
{
    LL ret = 0;
    if (i==N) {
       // OK[i0] = true;
        return 1;
    }
    int need = t * Q[i][0];
  //  prt(need);
    int j = lower_bound(Q[i]+1, Q[i]+P+1, need*0.9) - Q[i];
    for (; j<=P && Q[i][j]<=need*1.1; j++) if (!used[i][j]) {
        used[i][j] = true;
        int tmp = dfs(i+1, t);
        ret += tmp;
        if (tmp == 0) used[i][j] = false;
    }
    return ret;
}
int main()
{
    int re, ca = 1; cin>>re;
    while (re--) {
        cin >>N>>P;
        memset(used,0,sizeof used);
        for (int i=0;i<N;i++) cin>>R[i];
       // sort(R, R+N);
        for (int i=0;i<N;i++) {
        /*    for (int j=0;j<P;j++) {
                cin>>Q[i][j];
            } */
            for (int j=1;j<=P;j++) {
                cin>>Q[i][j];
            }
            sort(Q[i]+1, Q[i]+P+1); Q[i][0] = R[i];
          //  sort(Q, Q+P);
        }
        for (int i=0;i<N;i++) {
            for (int j=i+1;j<N;j++) if (Q[i][0] > Q[j][0]) {
                for (int k=0;k<=P;k++) swap(Q[i][k], Q[j][k]);
            }
        }
        for (int i=0;i<N;i++) R[i] = Q[i][0];
        LL ans = 0;
        int t = 1; int x = Q[0][0];
        for (int ii=1;ii<=P;ii++) {
            int L = Q[0][ii] / 1.1, H = Q[0][ii] / 0.9 + 0.99;
           // prt(L); prt(H);
            vector<Z> vec;
            x = Q[0][ii];
            vec.push_back(Z(0,ii));
          //  prt(R[0]);
         //   prt(x);
            for (int t=L/R[0]; t<= H/R[0]; t++) if(t*R[0]*0.9 - 0.01<=x && x<=t*R[0]*1.1) {
             //   prt(t);
                bool ok = true;
                for (int i=1;i<N;i++) {
                    int need = t * Q[i][0];
                    int j = lower_bound(Q[i]+1, Q[i]+P+1, need*0.9) - Q[i];
                    while (j<=P && Q[i][j]<=x*1.1 && used[i][j]) j++;
                    if (!(j<=P && Q[i][j]<=need*1.1)) {
                        for (Z x : vec) used[x.first][x.second] = false;
                        ok = false; break;
                    }
                    used[i][j] = true;
                    vec.push_back(Z(i,j));
                }
             //   puts("===");
                if (ok) { ans ++; break; }
            }
        }

        printf("Case #%d: ", ca++);
        cout<<ans<<endl;
    }
    return 0;
}
/**
64

2 1
500 300
900
660

2 1
500 300
1500
809

2 2
50 100
450 449
1100 1101

2 1
500 300
300
500

1 8
10
11 13 17 11 16 14 12 18

3 3
70 80 90
1260 1500 700
800 1440 1600
1700 1620 900

3 3
70 80 90
700 1260 1500
800 1440 1600
900 1620 1700

*/
