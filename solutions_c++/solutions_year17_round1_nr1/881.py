#include <bits/stdc++.h>
#define prt(k) cerr<<#k" = "<<k<<endl
#define pln(k) cout<<#k" = "<<k<<endl;
typedef long long LL;
const int INF = 0x3f3f3f3f;
void read(int &re) { scanf("%d", &re); }
using namespace std;
int R, C;
bool r[555], c[555];
char a[55][55];

int main()
{
    int re, ca = 1; cin>>re;
    while (re--) {
        cin >> R >> C;
        memset(a,0,sizeof a);
        for (int i=0;i<R;i++) scanf("%s", a[i]);
        memset(r,0,sizeof r);
        memset(c, 0, sizeof c);
        for (int i=0;i<R;i++) {
            for (int j=0;j<C; j++) if (isalpha(a[i][j])) {
                r[i] = true;
                c[j] = true;
            }
        }
        for (int i=0;i<R;i++) {
            for (int j=0;j<C; j++) if (isalpha(a[i][j])) {
                int t = i+1;
                while (t<R && !r[t]) t++;
                int li = i-1;
                while (li>=0 && !r[li]) li--;
                int jj = j+1;
                while (jj<C && a[i][jj]=='?') jj++;
                int lj = j-1;
                while (lj>=0 && a[i][lj]=='?') lj--;
             //   if (lj<0) lj=0;
                char ch = a[i][j];
                for (int x=li+1;x<t;x++) {
                    for (int b=lj+1;b<jj;b++) {
                        a[x][b] = a[i][j];
                    }
                }
            }
        }
        printf("Case #%d:\n", ca++);
        for (int i=0;i<R;i++) cout<<a[i]<<endl;
    }
    return 0;
}
