
#include <bits/stdc++.h>
using namespace std;
#define md int(1600)
#define inf int(1e9+100)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b ;i++)
#define DOW(i,b,a) for(int i=(b),_a=(a); i>=_a ;i--)
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define pii pair<int,int>
#define ll long long

int xx[4]={0,0,1,-1};
int yy[4]={1,-1,0,0};
int a[md];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int tcase;
    scanf("%d",&tcase);
    FOR(o,1,tcase)
    {
        int cnt=0;
        printf("Case #%d: ",o);
        ll x;
        scanf("%lld",&x);
        memset(a,0,sizeof(a));
        while (x!=0)
        {
            cnt++;
            a[cnt]=x%10;
            x/=10;
        }
        int vt=cnt;
        bool t=true;
        DOW(i,cnt,1)
        if (a[i]>=a[i+1])
        {
            if (a[i]>a[i+1])
            {
                vt=i;
            }
        }
        else
        {
            t=false;
            break;
        }
        if (t==false)
        {
            a[vt]-=1;
            DOW(i,vt-1,1)
            a[i]=9;
        }
        DOW(i,cnt,1)
        if (i==cnt && a[i]==0)
        {

        }
        else
        printf("%d",a[i]);

        printf("\n");
    }
}
