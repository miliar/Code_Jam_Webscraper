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

priority_queue<double,vector<double>,greater<double>> pq;

int main()
{
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    freopen("00_input.txt","r",stdin);freopen("00_output.txt","w",stdout);
    //pf("Hello World\n");
    int t,i,j,n,k,counter;
    double u,val,need,res;
    sf("%d",&t);
    for(i=0;i<t;i++)
    {
        sf("%d %d",&n,&k);
        sf("%lf",&u);
        for(j=0;j<n;j++)
        {
            sf("%lf",&val);
            pq.push(val);
        }
        val = pq.top();
        counter = 1;
        pq.pop();
        while(!pq.empty())
        {
            //cout << val << endl;
            if(pq.top()==val)
            {
                counter++;
                pq.pop();
            }
            else
            {
                need = pq.top() - val;
                need *= counter;
                //cout << pq.top() << " " << need << " " << u << endl;
                if(need<=u)
                {
                    val = pq.top();
                    pq.pop();
                    counter += 1;
                    u -= need;
                }
                else
                {
                    need = u/counter;
                    val += need;
                    goto here;
                }
            }
        }
        need = u/counter;
        val += need;
        here:
        res = 1.0;
        for(j=0;j<counter;j++)
        {
            res *= val;
        }
        while(!pq.empty())
        {
            res *= pq.top();
            pq.pop();
        }
        pf("Case #%d: %.8f\n",i+1,min(res,1.0));
    }
}
