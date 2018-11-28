#include <stdio.h>
#include <iostream>
#include <queue>
#include <string>
#include <algorithm>
#include <cstdio>
#include <stack>
#include <vector>
#include <map>
#include <ctime>
#include <string.h>
#define inf 0x7fffffff
using namespace std;
//1232
long long a,b,c,n,m,l[110010],o[120010],k,i,d,dx[10]={0,1,0,1,0,-1,-1,1,1},dy[10]={0,0,1,1,1,1,-1,1,-1};
long long x,y,z;
stack<int> s;
struct P
{
    int x,y;
    long long z;
    bool operator<(const P &a)const
    {
        return y>a.y;
    }
};
 //map<int, int> p;
queue<P> q;
string r;
vector<P> v[1000100];
vector<long long> j[1000100];
bool sdf(P a,P b){return a.y<b.y;}

int f(int t)
{
    int h=t;
    for(;h>0;h/=10)
        if(h%10<(h/10%10)) break;

    if(h==0) return t;
    else return f(t-1);
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&a);
    for(int t=1;t<=a;t++)
    {
        scanf("%d",&b);
        printf("Case #%d: %d\n",t,f(b));
    }
    return 0;
}
