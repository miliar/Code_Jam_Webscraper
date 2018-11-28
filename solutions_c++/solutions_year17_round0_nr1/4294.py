/**
* @author Ashini Singha
* IIT,Jahangirnagar University
*/
#include<bits/stdc++.h>
using namespace std;
#define     ll          long long int
#define     fo(i,b,n)   for(int i=(b); i<(n) ; i++)
#define     xx          first
#define     yy          second
#define     pb          push_back
#define     sz(n)       int(n.size())
#define     pii         pair
#define     MP          make_pair
#define     PI          acos(-1.0)

#define read(x)         scanf("%d",&x)
#define read2(x,y)      scanf("%d%d",&x,&y)
#define readl(x)        scanf("%lld",&x)
#define readl2(x,y)     scanf("%lld%lld",&x,&y)
#define readd(x)        scanf("%lf",&x)
#define readd2(x,y)     scanf("%lf%lf",&x,&y)

#define pr(n)           printf("%d",n)
#define prn(n)          printf("%d\n",n)
#define prl(n)          printf("%lld",n)
#define prln(n)         printf("%lld\n",n)
#define prd(x)          printf("%lf",x)
#define prdn(x)         printf("%lf\n",x)
#define TC(n) printf("Case %d: ",n)
/*_____________E_N_D______________*/

const int N = 1005;
char s[N];

int main()
{
      freopen("IN.txt","r",stdin);
      freopen("OUT.txt","w",stdout);

      int t;
      read(t);
      fo(tc, 1, t + 1) {
            int k;
            scanf("%s %d", s, &k);
            int n = strlen(s);
            int cnt = 0;

            fo(i, 0, n - k + 1) {
                  if(s[i] == '-') {
                        cnt++;
                        fo(j, 0, k) {
                              if(s[i + j] == '+')
                                    s[i + j] = '-';
                              else s[i + j] = '+';
                        }
                  }
            }

            int c = 0;
            fo(i, 0, n) c += (int) (s[i] == '+');
            printf("Case #%d: ", tc);
            if(c == n) prn(cnt);
            else puts("IMPOSSIBLE");
      }

      return 0;
}

















