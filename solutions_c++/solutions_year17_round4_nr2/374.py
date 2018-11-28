#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>
#include<assert.h>
using namespace std;
#define ull unsigned long long
const int maxn = 2000;
int a[maxn] , b[maxn];
int t;int T,n,c,m;
bool cal(int s){
    t = 0;
    int k = 0;
//    printf("s %d\n",s);
    for(int i=1;i<=n;i++){
        k += a[i];
//        printf("k %d ",k);
        if( k > s * i )
            return false;
        if( a[i] > s )
            t += a[i] - s;
    }
    return true;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    int CASE = 0,anst;
    while(T--){
        scanf("%d%d%d",&n,&c,&m);
        int x,y;
        memset(a,0,sizeof a);
        memset(b,0,sizeof b);
        for(int i=0;i<m;i++){
            scanf("%d%d",&x,&y);
            a[x]++;
            b[y]++;
        }
        int ans = 0;
        for(int i=1;i<=c;i++)
            ans = max(ans,b[i]);
        int l = ans , r = m;
//        for(int i=1;i<=n;i++)
//            printf("%d ",a[i]); puts("");
        ans = m + 1;
//        printf("%d %d\n",l,r);
        while( l <= r ){
            int mid = l+r>>1;
            if( cal(mid) ){
                r = mid-1;
                if( ans > mid ){
                    ans = mid;
                    anst = t;
                }
            }else l = mid+1;
        }
        printf("Case #%d: %d %d\n",++CASE,ans,anst);
    }
    return 0;
}
