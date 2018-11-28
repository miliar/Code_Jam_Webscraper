#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;
int T_T;
int n;
int R,O,Y,G,B,V;
int str[10000];
int main(void)
{
    #ifdef LOCAL
    freopen("B-large.in","r",stdin);
    freopen("out-large.txt","w",stdout);
    #endif
    scanf("%d",&T_T);
    for (int cas=1;cas<=T_T;cas++)
    {
        scanf("%d%d%d%d%d%d%d",&n,&R,&O,&Y,&G,&B,&V);
//        printf("n = %d R = %d O = %d Y = %d G = %d B = %d V = %d\n",n,R,O,Y,G,B,V);
        printf("Case #%d: ",cas);

        if (G == R && O+Y+B+V == 0) {
            for (int i=0;i<G;i++) printf("GR");
            puts("");
            continue;
        } else if (V == Y && G+R+B+O == 0) {
            for (int i=0;i<V;i++) printf("VY");
            puts("");
            continue;
        } else if (B == O && G+R+V+Y == 0) {
            for (int i=0;i<B;i++) printf("BO");
            puts("");
            continue;
        }

        if ((G && R <= G) || (V && Y <= V) || (O && B <= O)) {
            printf("IMPOSSIBLE\n");
            continue;
        }
//        printf("B = %d, O = %d\n",B,O);
        int a[3] = {R-G,Y-V,B-O}, cur = 0, t;
//        printf("%d %d %d\n",a[0],a[1],a[2]);
        char s[8] = "RYB";
        bool flag = true;
        for (int i=0;i<3;i++) if (a[i] > 0) {
            str[cur++] = s[i];
            a[i]--;
            t = i;
            break;
        }
        while (a[0] || a[1] || a[2]) {
            int x=(t+1)%3, y=(t+2)%3;
            if (a[x]==0 && a[y]==0) {
                flag = false;
                break;
            }
            if (a[x]>a[y] || (a[x]==a[y] && s[x]==s[0])) str[cur++]=s[x],a[x]--,t=x;
            else str[cur++]=s[y],a[y]--,t=y;
        }
        if (flag == false || str[0]==str[cur-1]) {
            printf("IMPOSSIBLE\n");
            continue;
        }

//        for (int i=0;i<cur;i++) printf("%c",str[i]); puts("");

        int fR = 1, fY = 1, fB = 1;
        for (int i=0;i<cur;i++) {
            if (fR && str[i] == 'R') {
                printf("R");for (int j=0;j<G;j++) printf("GR");
                fR = 0;
            } else if (fY && str[i] == 'Y') {
                printf("Y");for (int j=0;j<V;j++) printf("VY");
                fY = 0;
            } else if (fB && str[i] == 'B') {
                printf("B");for (int j=0;j<O;j++) printf("OB");
                fB = 0;
            } else printf("%c",str[i]);
        }
        puts("");
    }
    return 0;
}
