#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <cmath>
#include <bitset>
using namespace std;

#define pi pair<int,int>
#define mp(x,y) make_pair(x,y)
#define fi first
#define se second
#define pl pair<long long,long long>
#define pb push_back
#define vi vector<int>
#define ll long long
#define ALL(c) c.begin(),c.end()
#define VAR(v,n) __typeof(n) v=(n)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)

const int MAXN=1005;
char t[20];

int main ()
{
    int a,b,c,d,e,f,g,z;
    ll k,n,i1,i2;

    scanf ("%d", &z);

    for (a=1; a<=z; a++)
    {
        scanf("%lld%lld", &n, &k);
        i1=1;
        i2=0;

        while (1)
        {
            if (k<=i1)
            {
                printf ("Case #%d: %lld %lld\n", a, n/2, (n-1)/2);
                break;
            }

            k-=i1;

            if (k<=i2)
            {
                printf ("Case #%d: %lld %lld\n", a, (n-1)/2, (n-2)/2);
                break;
            }

            k-=i2;

            if (n%2)
                i1=i1*2+i2;
            else
                i2=i2*2+i1;

            n/=2;
        }
    }

    return 0;
}
