#include <bits/stdc++.h>
using namespace std;
#define M_PI 3.14159265358979323846
#define md int(1e5+100)
#define mq int(1e3+100)
#define inf int(1e9+100)
#define modul int(1e9+7)
#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b ;i++)
#define DOW(i,b,a) for(int i=(b),_a=(a); i>=_a ;i--)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define pb push_back
#define pii pair<int,int>
#define ll long long
struct re
{
    int r,h;
};

int tcase;
int n,k;
re a[md];

bool cmp(re a, re b)
{
    return a.r<b.r;
}
double sqr(double x)
{
    return x*x;
}

bool cmp2(re a , re b)
{
    return double(a.r)*a.h >double(b.r)*b.h;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&tcase);
    FOR(o,1,tcase)
    {
        scanf("%d%d",&n,&k);
        FOR(i,1,n)
        scanf("%d%d",&a[i].r,&a[i].h);
        sort(a+1,a+1+n,cmp);

        double res=0;
        FOR(i,k,n)
        {
            double ts= M_PI*sqr(a[i].r)+2*M_PI*double(a[i].r)*a[i].h;
            sort(a+1,a+i,cmp2);

            FOR(j,1,k-1)
            {
                ts+=2*M_PI*double(a[j].r)*a[j].h;
            }
            res=max(res,ts);
        }
        printf("Case #%d: %.7f\n",o,res);
    }
}

