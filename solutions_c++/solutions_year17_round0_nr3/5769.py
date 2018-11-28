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
#define sqr(x) (x*x)
#define gcd(x,y) __gcd((lol)abs(x),(lol)abs(y))
#define lcm(x,y) abs(x)/__gcd((lol)abs(x),(lol)abs(y))*abs(y)
#define logB(val,base) log(val)/log(base)

int dirK[8][2] = {{-2,1},{-1,2},{1,2},{2,1},{2,-1},{-1,-2},{1,-2},{-2,-1}};
int dir8[8][2] = {{-1,0},{0,1},{1,0},{0,-1},{-1,-1},{1,1},{1,-1},{-1,1}};
int dir4[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};
int month[] = {31,28,31,30,31,30,31,31,30,31,30,31};

/*============================================================================//
                                   send nudes
//============================================================================*/

char line[1005];
int n;

int getL(int pos)
{
    int counter = 0;
    while(pos>0&&line[pos-1]=='0')
    {
        pos--;
        counter++;
    }
    return counter;
}

int getR(int pos)
{
    int counter = 0;
    while(pos<n-1&&line[pos+1]=='0')
    {
        pos++;
        counter++;
    }
    return counter;
}

void call(int c,int k)
{
    int highPos,highL,highR,l,r;
    memset(line,'0',sizeof(line));
    for(int i=0;i<k;i++)
    {
        highL = -1;
        highR = -1;
        for(int j=0;j<n;j++)
        {
            if(line[j]=='0')
            {
                l = getL(j);
                r = getR(j);
                if(min(l,r)>min(highL,highR)||(min(l,r)==min(highL,highR)&&max(l,r)>max(highL,highR)))
                {
                    highPos = j;
                    highL = l;
                    highR = r;
                }
            }
        }
        line[highPos] = '1';
        //pf("%d ",highPos);
    }
    pf("Case #%d: %d %d\n",c+1,max(highL,highR),min(highL,highR));
}

int main()
{
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    freopen("00_input.txt","r",stdin);freopen("00_output.txt","w",stdout);
    //pf("Hello World\n");
    int t,i,k;
    sf("%d",&t);
    //getchar();
    for(i=0;i<t;i++)
    {
        sf("%d %d",&n,&k);
        call(i,k);
    }
}
