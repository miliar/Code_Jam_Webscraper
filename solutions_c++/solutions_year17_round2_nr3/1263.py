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
                      send nudes(well figured girls only!)
//============================================================================*/

struct POS
{
    int remain,speed,city,id;
    double cost;
    bool operator < (const POS &pos)const
    {
        return cost > pos.cost;
    }
}pos,nxt;

#define graphRange 105
int graph[graphRange+1][graphRange+1];
int horse[graphRange+1],speed[graphRange+1];
double dist[graphRange+1];

void dijkstra(int start,int n)
{
    fill(dist,dist+graphRange,1000000000000000.0);
    pos.remain = 0;
    pos.speed = 0;
    pos.city = start;
    pos.cost = 0;
    pos.id = start;
    priority_queue<POS> pq;
    pq.push(pos);
    while(!pq.empty())
    {
        pos = pq.top();
        pq.pop();
        for(int i=0;i<n;i++)
        {
            if(graph[pos.city][i]>0)
            {
                if(graph[pos.city][i]<=pos.remain)
                {
                    nxt.city = i;
                    nxt.speed = pos.speed;
                    nxt.remain = pos.remain - graph[pos.city][i];
                    nxt.cost = pos.cost + (1.0*graph[pos.city][i]/pos.speed);
                    nxt.id = pos.id;
                    pq.push(nxt);
                    //cout << nxt.city << " " << nxt.cost << " " << nxt.speed << " " << nxt.id << " " << nxt.remain << endl;
                }
                if(dist[pos.city]>pos.cost)
                {
                    nxt.city = i;
                    nxt.speed = speed[pos.city];
                    nxt.remain = horse[pos.city] - graph[pos.city][i];
                    nxt.cost = pos.cost + (1.0*graph[pos.city][i]/nxt.speed);
                    nxt.id = pos.city;
                    pq.push(nxt);
                    //cout << nxt.city << " " << nxt.cost << " " << nxt.speed << " " << nxt.id << " " << nxt.remain << endl;
                }
            }
        }
        if(dist[pos.city]>pos.cost)
        {
            dist[pos.city] = pos.cost;
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    freopen("00_input.txt","r",stdin);freopen("00_output.txt","w",stdout);
    //pf("Hello World\n");
    int t,i,j,k,n,q,start,finish;
    sf("%d",&t);
    for(i=0;i<t;i++)
    {
        sf("%d %d",&n,&q);
        for(j=0;j<n;j++)
        {
            sf("%d %d",&horse[j],&speed[j]);
        }
        for(j=0;j<n;j++)
        {
            for(k=0;k<n;k++)
            {
                sf("%d",&graph[j][k]);
            }
        }
        pf("Case #%d:",i+1);
        for(j=0;j<q;j++)
        {
            sf("%d %d",&start,&finish);
            dijkstra(start-1,n);
            pf(" %.8f",dist[finish-1]);
            /*for(k=0;k<n;k++)
            {
                pf(" %.8f",dist[k]);
            }*/
        }
        pf("\n");
    }
}
