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
using namespace std;
deque<pii>v;
long double sc,d;
int x,y,t,T,n,i,e;
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);

    for(t=1; t<=T; t++) {
        scanf("%d%d",&e,&n);
        sc=0.0;
        d=e;
        for(i=1; i<=n; i++)
        {
            scanf("%d%d",&x,&y);
            sc=max(sc,1.0*(d-x)/y);
        }
        d/=sc;
        printf("Case #%d: ",t);
       cout<<fixed<<setprecision(10)<<d<<'\n';

    }

    return 0;
}
