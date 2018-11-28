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
ll  n,m1,m2;
string s;
ll l,r;
struct wgh
{
    ll num,length;
};
queue <wgh> a;
wgh b,b1,b2,btemp;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>n;
    ll T=0;
    while(n--)
    {
        printf("Case #%lld: ",++T);
        cin>>m1>>m2;
        ll ans1=0,ans2=0;
        while(!a.empty())
            a.pop();
        b.length=m1;
        b.num=1;
        a.push(b);
        b1.length=0;
        b1.num=0;
        b2.length=0;
        b2.num=0;
        while(m2>0&&!a.empty())
        {
            while(m2>0&&!a.empty())
            {
                b=a.front();
                m2-=b.num;
                a.pop();
                r=(b.length)/2;
                l=(b.length-1)/2;
                if(r==b1.length)
                {
                    if(l==b2.length)
                    {
                        b1.num+=b.num;
                        b2.num+=b.num;
                    }
                    else
                    {
                        b1.num+=b.num;
                        a.push(b1);
                        b1=b2;
                        b2.length=l;
                        b2.num=b.num;
                    }
                }
                else
                {
                    if(r==b2.length)
                    {
                        b2.num+=b.num;
                        a.push(b1);
                        b1=b2;
                        b2.length=l;
                        b2.num=b.num;
                    }
                    else
                    {
                        if(b1.num)
                        a.push(b1);
                        if(b2.num)
                        a.push(b2);
                        b1.length=r;
                        b1.num=b.num;
                        b2.length=l;
                        b2.num=b.num;
                    }
                }
            }
            if(b1.num)
            a.push(b1);
            if(b2.num)
            a.push(b2);
            b1.length=0;
            b1.num=0;
            b2.length=0;
            b2.num=0;
        }
        if(!a.empty())
        printf("%lld %lld\n",r,l);
        else
            printf("0 0\n");
    }
    return 0;
}
