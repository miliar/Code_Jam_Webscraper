typedef long long ll;
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <utility>
#define pb push_back
#define mp make_pair
#define pll pair<ll,ll> 
#define plll pair<ll,pair<ll,ll> >

using namespace std;
struct point{
    ll di,s;
};
point a[1007];
bool cmp(point x,point y)
{
    return x.di>y.di;
}
int main()
{
    ll t,i,n,w=1,d;
    double ti,maxi;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld %lld",&d,&n);
        for(i=0;i<n;i++)
        scanf("%lld %lld",&a[i].di,&a[i].s);
        sort(a,a+n,cmp);
        maxi=0;
        for(i=0;i<n;i++)
        {
            ti=(double)(d-a[i].di)/a[i].s;
            maxi=max(maxi,ti);
        }
        printf("Case #%lld: %.6lf\n",w++,d/maxi);
    }
	return 0;
}