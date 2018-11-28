#include <bits/stdc++.h>
using namespace std;
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

int tcase;
int n;
int s;
double a[md],u;
int main()
{
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&tcase);
    FOR(o,1,tcase)
    {
        scanf("%d%d",&n,&s);
        scanf("%lf",&u);

        FOR(i,1,n)
        scanf("%lf",&a[i]);

        sort(a+1,a+1+n);
        a[n+1]=1;
        FOR(i,1,n)
        {
            double ts=a[i+1]-a[i];

            double k=0;
            if (i*ts>u)
            {
                k=u/i;
            }
            else k=ts;

            FOR(j,1,i)
            a[j]+=k;

            u-=k*i;

            if (u==0) break;
        }

        double res=1;
        FOR(i,1,n)
        res*=a[i];
        printf("Case #%d: %.7f\n",o,res);
    }
}

