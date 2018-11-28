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

void f(int t,int w)
{
    if(t==0)
    {
        puts("INSOMNIA");
        return;
    }
    for(int h=t*w;h>0;h/=10)
    {
        if(!l[h%10])
            l[h%10]=1,k++;
    }
    if(k==10)
    {
        printf("%d\n",w*t);

        return;
    }
    f(t,w+1);
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&a);
    for(int t=1;t<=a;t++)
    {
        cin>>r;
        k=0;
        i=0;
        scanf("%d",&b);
        for(int w=0;w<=r.size()-b;w++)

        if(r[w]=='-')
        {
            k++;
        for(int h=w;h<w+b;h++)
        {
            if(r[h]=='-')
                r[h]='+';
            else r[h]='-';
        }
        }
        for(int w=r.size()-b+1;w<r.size();w++)
                if(r[w]=='-')
                {
                    i=1;
                    break;
                }
        if(i==0)
        printf("Case #%d: %d\n",t,k);
        else
            printf("Case #%d: IMPOSSIBLE\n",t);
    }
    return 0;
}
