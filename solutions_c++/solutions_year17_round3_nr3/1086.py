#define _USE_MATH_DEFINES
#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define mt make_tuple
#define ll long long
#define pii pair<int,int>
#define tii tuple <int,int,int>
#define N 100005
#define mod 2000003
#define X first
#define Y second
#define eps 0.0000000001
#define all(x) x.begin(),x.end()
#define tot(x) x+1,x+n+1
#define M_PI 3.14159265358979323846
using namespace std;
int t,T,i,n,k;
long double prob,p[55],u,s;
void gp(int l,int r,long double s) {
    long double m=s/(r-l+1);
    bool ok=1;

    while(p[r]>m) {
        ok=0;
        s-=p[r];
        r--;
    }

    if(ok) {
        for(; l<=r; l++)
            p[l]=m;
    }
    else
        gp(l,r,s);
    }
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);

    for(t=1; t<=T; t++) {
        scanf("%d%d",&n,&k);
        cin>>u;
        s=0.0;

        for(i=1; i<=n; i++) {
            cin>>p[i];
            s+=p[i];
        }

        sort(tot(p));
        s+=u;
        gp(1,n,s);
        prob=1;

        for(i=1; i<=n; i++)
            prob*=p[i];
        printf("Case #%d: %lf\n",t,prob);
    }

    return 0;
}
