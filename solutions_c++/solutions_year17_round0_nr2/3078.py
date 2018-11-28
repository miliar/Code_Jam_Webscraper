#include <iostream>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
#define ll long long
ll  n,m;
string s;
ll a[20];
ll l;
bool judge()
{
    bool flag=true;
    ll o=a[1];
    for(ll i=2;i<=l;i++)
    {
        if(o<a[i]||a[i]<0)
        {
            return false;
        }
        o=a[i];
    }
    return true;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>n;
    ll T=0;
    while(n--)
    {
        printf("Case #%lld: ",++T);
        cin>>m;
        ll ans=0;
        l=0;
        while(m)
        {
            l++;
            a[l]=m%10;
            m/=10;
        }
        for(ll i=1;i<=l&&judge()==false;i++)
        {
            a[i]=9;
            a[i+1]--;
        }
        ll u=1;
        for(ll i=1;i<=l;i++)
        {
            ans+=u*a[i];
            u*=10;
        }
        printf("%lld\n",ans);
    }

    return 0;
}
