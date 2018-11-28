#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define pll pair<long long,long long>
#define mp make_pair

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int t;
    long long n,k;
    pll x,y,x1,y1;
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        cin>>n>>k;
        x=mp(n,1);
        y=mp(n+1,0);
        printf("Case #%d: ",cas);
        while (true)
        {
            y1=mp((y.first-1)-(y.first-1)/2,0);
            x1=mp((x.first-1)/2,0);
            if (k<=y.second)
            {
                printf("%I64d %I64d\n",(y.first-1)-(y.first-1)/2,(y.first-1)/2);
                break;
            }
            k-=y.second;
            y1.second+=y.second;
            if (y1.first==(y.first-1)/2) y1.second+=y.second;
            else x1.second+=y.second;
            if (k<=x.second)
            {
                printf("%I64d %I64d\n",(x.first-1)-(x.first-1)/2,(x.first-1)/2);
                break;
            }
            k-=x.second;
            x1.second+=x.second;
            if (x1.first==(x.first-1)-(x.first-1)/2) x1.second+=x.second;
            else y1.second+=x.second;
            x=x1;
            y=y1;
        }
    }
    return 0;
}
