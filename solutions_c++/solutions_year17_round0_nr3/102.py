#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>
#define LL long long
using namespace std;
int T_T;
LL n,k;
struct node
{
    LL len,cnt;
}a[1001000];
int head,tail;
int main(void)
{
//    freopen("c.in","r",stdin);
    freopen("C-large.in","r",stdin);
    freopen("out-large.txt","w",stdout);
    scanf("%d",&T_T);
    for (int cas=1;cas<=T_T;cas++)
    {
        scanf("%lld%lld",&n,&k);
        //printf("n = %lld, k = %lld\n",n,k);
        LL mn,mx;
        head = tail = 0;
        a[tail++] = (node){n,1};
        for (LL i=k;i>0;)
        {
            i -= a[head].cnt;
            LL len = a[head].len-1;
            mn = len/2;
            mx = len/2+len%2;
            if (a[tail-1].len == mx) {
                a[tail-1].cnt += a[head].cnt;
            } else {
                a[tail++] = (node){mx,a[head].cnt};
            }
            if (a[tail-1].len == mn) {
                a[tail-1].cnt += a[head].cnt;
            } else {
                a[tail++] = (node){mn,a[head].cnt};
            }
            head++;
            //printf("tail = %d\n",tail);
            //printf("left %lld\n",i);
//            for (int j=head;j<tail;j++) printf("(%lld,%lld) ",a[j].len,a[j].cnt);
//            puts("");
        }
        //printf("tail = %d\n",tail);
        printf("Case #%d: %lld %lld\n",cas,mx,mn);
    }
    return 0;
}

