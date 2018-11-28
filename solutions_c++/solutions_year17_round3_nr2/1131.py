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

struct MYTIME
{
    int start,finish;
};

pii myTime[5];

int main()
{
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    freopen("00_input.txt","r",stdin);freopen("00_output.txt","w",stdout);
    //pf("Hello World\n");
    int t,i,j,n,k,ac,aj;
    sf("%d",&t);
    for(i=0;i<t;i++)
    {
        sf("%d %d",&ac,&aj);
        n = ac + aj;
        for(j=0;j<n;j++)
        {
            sf("%d %d",&myTime[j].first,&myTime[j].second);
        }
        if(n==1||ac==1)
        {
            pf("Case #%d: 2\n",i+1);
        }
        else
        {
            sort(myTime,myTime+n);
            if(myTime[1].first-myTime[0].second>=720)
            {
                pf("Case #%d: 2\n",i+1);
            }
            else if(myTime[1].second-myTime[0].first<=720)
            {
                pf("Case #%d: 2\n",i+1);
            }
            else
            {
                pf("Case #%d: 4\n",i+1);
            }
        }
    }
}
