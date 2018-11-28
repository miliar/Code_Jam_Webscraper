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
char s[md];
int a[md];
int n,k;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int tcase;
    scanf("%d",&tcase);
    FOR(o,1,tcase)
    {
        scanf("%s",s+1);
        scanf("%d",&k);
        n=strlen(s+1);
        FOR(i,1,n)
        if (s[i]=='-') a[i]=0;
        else a[i]=1;
        bool t=true;
        int dem=0;
        FOR(i,1,n)
        if (a[i]==0)
        {
            if (i>n-k+1) { t=false; break;}
            dem++;
            FOR(j,0,k-1)
            a[i+j]=1-a[i+j];
        }
        if (!t) printf("Case #%d: IMPOSSIBLE\n",o);
        else printf("Case #%d: %d\n",o,dem);
    }
}

