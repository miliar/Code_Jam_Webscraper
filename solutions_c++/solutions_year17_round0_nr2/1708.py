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
    int a,b,c,d,e,f,g,z,n,k;
    ll w;

    scanf ("%d", &z);

    for (a=1; a<=z; a++)
    {
        scanf("%s", t);

        for (b=0; t[b]; b=c)
        {
            for (c=b+1; t[b]==t[c]; c++);

            if (t[c] && t[c]<t[b])
                break;
        }

        w=0;

        for (d=0; d<b; d++)
            w=w*10+t[d]-'0';

        if (t[d])
        {
            w=w*10+t[d]-'1';
            d++;
        }

        for (; t[d]; d++)
            w=w*10+9;

        printf ("Case #%d: %lld\n", a, w);
    }

    return 0;
}
