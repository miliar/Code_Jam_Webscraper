//#include <bits/stdc++.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <bitset>
#include <utility>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <iostream>
#include <iomanip>

using namespace std;

typedef long long lol;
typedef pair<int,int> pii;
typedef map<int,int> mii;

#define pf printf
#define sf scanf
#define pause system("pause")
#define pmin int,vector<int>,greater<int>
#define checkBit(n,p) (bool)(n&(1<<p))
#define setBit(n,p) (n|=(1<<p))
#define resetBit(n,p) (n&=~(1<<p))
#define toggleBit(n,p) (n^=1<<p)
#define mp make_pair
#define pb push_back
#define PI acos(-1.0)
#define sqr(x) ((lol)x*x)
#define gcd(x,y) __gcd((lol)abs(x),(lol)abs(y))
#define lcm(x,y) abs(x)/__gcd((lol)abs(x),(lol)abs(y))*abs(y)
#define logB(val,base) log(val)/log(base)

int dirK[8][2] = {{-2,1},{-1,2},{1,2},{2,1},{2,-1},{1,-2},{-1,-2},{-2,-1}};
int dir8[8][2] = {{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1}};
int dir4[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};
int month[] = {31,28,31,30,31,30,31,31,30,31,30,31};

/*============================================================================//
                        নোয়াখালী বিভাগ চাই - Lionel Messi
//============================================================================*/

double getH(int r,int h)
{
    double res = 2.0 * PI * r * h;
    return res;
}

double getB(int r)
{
    double res = 1.0 * PI * sqr(r);
    return res;
}

struct CAKE
{
    int r,h;
    double areaH,areaB;
};

CAKE cake[12];
vector<int> v;
double ans,high,res;

void combination(int n, int k)
{
    string bitmask(k,1);
    bitmask.resize(n,0);
    res = 0;
    do {
        ans = 0;
        high = 0;
        for (int i = 0; i < n; ++i)
        {
            if (bitmask[i])
            {
                ans += cake[i].areaH;
                if(high<cake[i].areaB)
                {
                    high = cake[i].areaB;
                }
            }
        }
        ans += high;
        res = max(res,ans);
    } while (std::prev_permutation(bitmask.begin(),bitmask.end()));
}

int main()
{
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    freopen("00_input.txt","r",stdin);freopen("00_output.txt","w",stdout);
    //pf("Hello World\n");
    int t,i,j,n,k;
    sf("%d",&t);
    for(i=0;i<t;i++)
    {
        v.clear();
        sf("%d %d",&n,&k);
        for(j=0;j<n;j++)
        {
            v.pb(j);
            sf("%d %d",&cake[j].r,&cake[j].h);
            cake[j].areaH = getH(cake[j].r,cake[j].h);
            cake[j].areaB = getB(cake[j].r);
        }
        combination(n,k);
        pf("Case #%d: %.8f\n",i+1,res);
    }
}
