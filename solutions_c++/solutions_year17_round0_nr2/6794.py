#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>


using namespace std;

#define pi acos(-1)
#define gcd(a,b) __gcd(a,b)
#define PB push_back
#define SIZE(x) (int)x.size()
#define clr(x,y) memset(x,y,sizeof(x))
#define MP(x,y) make_pair(x,y)
#define ALL(t) (t).begin(),(t).end()
#define FOR(i,n,m) for (int i = n; i <= m; i ++)
#define ROF(i,n,m) for (int i = n; i >= m; i --)
#define RI(x) scanf ("%d", &(x))
#define RII(x,y) RI(x),RI(y)
#define RIII(x,y,z) RI(x),RI(y),RI(z)


typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;

const ll mod = 1e9+7;
const int INF = 1e9;
const double EPS = 1e-8;

/**************************************END************************************/

string a;

void change()
{
    int len=a.size();
    int jiewei=0;
    if(a[len-1]=='0')
    {
        a[len-1]='9';
        jiewei=1;
    }
    else
    {
        a[len-1]--;
    }
    for(int i=len-2;i>=0;i--)
    {
        if(jiewei)
        {
            jiewei=0;
            if(a[i]=='0')
            {
                a[i]='9';
                jiewei=1;
            }
            else
            {
                a[i]--;
            }
        }
        if(!jiewei)break;
    }
}
int main()
{
    
    freopen("/Users/apple/Desktop/B-small-attempt3.in","r",stdin);
    freopen("/Users/apple/Desktop/B-small-attempt3.out","w",stdout);
    int t;
    RI(t);
    int cas=1;
    while(t--)
    {

        cin>>a;
        int len=a.size();
        while(1)
        {
            int flag=1;
            for(int i=0;i<len-1;i++)
            {
                if(a[i]>a[i+1])
                {
                    flag=0;
                    break;
                }
            }
            if(flag)break;
            else
            {
                //cout<<a<<endl;
                change();
            }
        }

        printf("Case #%d: ",cas++);
        int i;
        for(i=0;i<len;i++)
        {
            if(a[i]!='0')break;
        }
        for(;i<len;i++)
        {
            cout<<a[i];
        }
        puts("");
    }
}