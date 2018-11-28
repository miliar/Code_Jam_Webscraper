#include<bits/stdc++.h>


using namespace std;

pair <double,double> pan[1010];

#define M_PI 3.14159265358979323846
double he[1010];
void solve ( int t )
{
    int n,k;
    scanf("%d%d",&n,&k);
    for ( int c=1 ; c<=n ; c++ )    scanf("%lf%lf",&pan[c].first,&pan[c].second);
    sort(pan+1,pan+1+n);
    double sol = 0;
    for ( int c=n ; c>=k ; c-- )
    {
        double r = pan[c].first,h=pan[c].second;
        //cout << r << endl;
        double ans = 2*M_PI*r*h + M_PI*r*r;
        for ( int d=c-1 ; d>=1 ; d-- )
        {
            r = pan[d].first,h=pan[d].second;
            he[d] = 2*M_PI*r*h;
        }
        sort(he+1,he+c);
        for ( int d=c-1 ; d>c-k ; d-- ) ans += he[d];
        sol = max ( sol , ans);
        //cout << ans << endl;
    }
    printf("Case #%d: %.12f\n",t,sol);
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for ( int c=1 ; c<=t ; c++ )    solve(c);
}
