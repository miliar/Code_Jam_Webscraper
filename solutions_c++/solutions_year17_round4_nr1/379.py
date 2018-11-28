#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <set>
#include <stack>
#include <queue>
#include <utility>
#include <bitset>
#include <cassert>
#define fi first
#define se second
#define mkp make_pair
#define pb push_back
#define rep(i,a,b) for (int i=(a);i<(b);i++)
#define per(i,b,a) for (int i=(b)-1;i>=(a);i--)
#define REP(i,a,b) for (int i=(a);i<=(b);i++)
#define PER(i,b,a) for (int i=(b);i>=(a);i--)
using namespace std;
typedef long long LL;

const int INF = 0x3f3f3f3f;

const int MAXN = 1000005; // 1e6;
int T,n,G[MAXN],P;
int main()
{
        freopen("A-large.in","r",stdin);
        freopen("Large_A.txt","w",stdout);
        scanf("%d",&T);
        rep(cas,1,T+1)
        {
                scanf("%d%d",&n,&P);
                rep(i,0,n) scanf("%d",&G[i]);
                rep(i,0,n) G[i]%=P;
                printf("Case #%d: ",cas);
                if(P == 2)
                {
                        int cnt = 0;
                        rep(i,0,n) cnt+=G[i];
                        cnt /= 2;

                        printf("%d\n",n-cnt);
                }
                else if (P == 3)
                {
                        int cnt[5];
                        memset(cnt,0,sizeof cnt);
                        int ans = 0;
                        rep(i,0,n) cnt[G[i]]++;
                        ans = min(cnt[1],cnt[2]);
                        cnt[1]-=ans, cnt[2]-=ans;
//                        cout<<ans<<" "<<n<<endl;
                        if (cnt[1] > 0)
                        {
                                ans += cnt[1]/3*2;
                                if (cnt[1] % 3 == 2) ans++;
                        }
                        if (cnt[2]>0)
                        {
                                ans += cnt[2]/3*2;
                                if (cnt[2] % 3 == 2) ans++;
                        }
                        printf("%d\n",n-ans);
                }
                else if (P == 4)
                {
                        int cnt[5];
                        memset(cnt,0,sizeof cnt);
                        int ans = 0;
                        rep(i,0,n) cnt[G[i]]++;
                        ans = min(cnt[1],cnt[3]);
                        cnt[1]-=ans,cnt[3]-=ans;
                        int q = max(cnt[1],cnt[3]);
                        if (2*cnt[2] >= q)
                        {
                                cnt[2]-=q/2;
                                ans += q/2*2;
                                q -= q/2*2;
                                ans += cnt[2]/2;
                                cnt[2] -= cnt[2]/2*2;
                                if (cnt[2]+q > 1) {ans++; assert(cnt[2]+q==2);}
                        }
                        else
                        {
                                q -= cnt[2]*2;
                                ans +=cnt[2]*2;
                                ans += q/4*3;
                                if (q%4 >= 2) ans += q%4-1;

                        }
                        printf("%d\n",n-ans);

                }
        }
}
