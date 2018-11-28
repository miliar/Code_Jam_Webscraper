#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

const int MAXN = 1000;


char str[MAXN + 5];
bool flip[MAXN + 5];
int n, K;

int main() {
    freopen("pancake.in","r",stdin);
    freopen("pancake.out","w",stdout);
    int c,c2;
    int tests;
    scanf("%d",&tests);
    for (int test=1;test<=tests;test++) {
        scanf("%s%d",str, &K);
        memset(flip,0,sizeof(flip));
        n = strlen(str);
        bool f = 0;
        int ret = 0;
        bool bad = false;
        for (int c=0;str[c];c++) {
            f ^= flip[c];
            if ((str[c] == '-') ^ f) {
                if (c + K > n) {
                    bad = true;
                    break;
                }
                ret++;
                f ^= 1;
                flip[c + K] = 1;
            }
        }
        printf("Case #%d: ",test);
        if (bad) printf("IMPOSSIBLE\n");
        else printf("%d\n",ret);
    }
    
    return 0;
}
