#include <bits/stdc++.h>
using namespace std;
const int MAXN=1005;
int T,D,N,dist,v1,d1,v2,d2;
double tt;
pair<int,int> horses[MAXN];
int main()
{
    //freopen("DATA.txt","r",stdin);
    freopen("cruise2.in","r",stdin);
    freopen("cruise2.out","w",stdout);
    scanf("%i",&T);
    for (int t=1;t<=T;t++)
    {
        scanf("%i%i",&D,&N);
        for (int i=0;i<N;i++)scanf("%i%i",&horses[i].first,&horses[i].second);
        sort(horses,horses+N);
        tt=0;
        for (int i=N-1;i>=0;i--)
        {
            tt=max(tt,(double)(D-horses[i].first)/horses[i].second);
        }
        printf("Case #%d: %.8f\n",t,D/tt);
    }
}
