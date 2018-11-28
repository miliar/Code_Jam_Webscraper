#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
int n,a[6];
int ans[2000];
bool exist_primary()
{
    return a[0] || a[2] || a[4];
}
bool exist_secondary()
{
    return a[1] || a[3] || a[5];
}
int largest_primary(int now)
{
    if (!now)
    {
        if (a[0]>=a[2] && a[0]>=a[4]) return 0;
        if (a[2]>=a[0] && a[2]>=a[4]) return 2;
        return 4;
    }
    int correlate=ans[now-1];
    if (correlate==0)
    {
        if (a[2]!=a[4]) return (a[2]>=a[4])?2:4;
        if (now>=n-2) return (ans[0]==2)?2:4;
        if (now>=2) return (ans[now-2]==2)?2:4;
        return 2;
    }
    else if (correlate==2)
    {
        if (a[0]!=a[4]) return (a[0]>=a[4])?0:4;
        if (now>=n-2) return (ans[0]==0)?0:4;
        if (now>=2) return (ans[now-2]==0)?0:4;
        return 0;
    }
    else
    {
        if (a[0]!=a[2]) return (a[0]>=a[2])?0:2;
        if (now>=n-2) return (ans[0]==0)?0:2;
        if (now>=2) return (ans[now-2]==0)?0:2;
        return 0;
    }
}
int largest_secondary(int now)
{
    if (!now)
    {
        if (a[1]>=a[3] && a[1]>=a[5]) return 1;
        if (a[3]>=a[1] && a[3]>=a[5]) return 3;
        return 5;
    }
    int correlate=(ans[now-1]+3)%6;
    if (correlate==1) return (a[3]>=a[5])?3:5;
    else if (correlate==3) return (a[1]>=a[5])?1:5;
    else return (a[1]>=a[3])?1:3;
}
bool reduce(int idx,int &now)
{
    if (!a[idx]) return false;
    a[idx]--;
    ans[now++]=idx;
    return true;
}
int main()
{
    //freopen("test.txt","r",stdin);
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    int testcases;
    scanf("%d",&testcases);
    for (int test=1;test<=testcases;test++)
    {
        scanf("%d",&n);
        for (int i=0;i<6;i++)
            scanf("%d",&a[i]);
        bool possible=true;
        int now=0;
        while (possible && exist_secondary() && now<n)
        {
            int idx=largest_secondary(now);
            int correlate=(idx+3)%6;
            if (now<n) possible&=reduce(correlate,now);
            while (possible && a[idx] && now<n)
            {
                if (now<n) possible&=reduce(idx,now);
                if (now<n) possible&=reduce(correlate,now);
            }
        }
        while (possible && exist_primary() && now<n)
        {
            int idx=largest_primary(now);
            if (now<n) possible&=reduce(idx,now);
        }
        if (abs(ans[now-1]-ans[0])<=1 || abs(ans[now-1]-ans[0])>=5) possible=false;
        printf("Case #%d: ",test);
        if (possible)
        {
            for (int i=0;i<n;i++)
                switch (ans[i])
                {
                    case 0:printf("R");break;
                    case 1:printf("O");break;
                    case 2:printf("Y");break;
                    case 3:printf("G");break;
                    case 4:printf("B");break;
                    case 5:printf("V");break;
                }
        }
        else printf("IMPOSSIBLE");
        printf("\n");
    }
    return 0;
}
