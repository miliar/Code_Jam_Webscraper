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

const int N = 1e6 + 5;
int vis[N];

#define dual_print(x,y) printf("%lld %lld\n",x,y);
#define cj_case(x) printf("Case #%d: ",x);

int main()
{
      freopen("in.txt","r",stdin);
      freopen("temp_out.txt","w",stdout);

      int t;
      read(t);
      fo(tc, 1, t + 1) {
            int n, k;
            read2(n, k);

            priority_queue<int>q;
            q.push(n);

            fo(i, 0, k - 1) {

                  int val = q.top();
                  q.pop();
                  int mid=(val/2);
                  if(val <= 1) {
                        q.push(0);
                        q.push(0);
                  } else if(val % 2 == 0) {
                        q.push(mid);
                        q.push(mid-1);
                  } else {
                        q.push(mid);
                        q.push(mid);
                  }

            }

            cj_case(tc);
            int val = q.top();
            if(val <= 1) {
                  dual_print(0, 0);
            } else if(val & 1) {
                  dual_print(val / 2, val / 2);
            } else {
                  dual_print(val / 2, val / 2 - 1);
            }



      }
      return 0;
}


















