#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;

int n,k;
struct Node
{
    int rad;
    int height;
    bool operator<(const Node& b) const
    {
        return rad>b.rad;
    }
};

Node node[1005];
double rec[1005][1005];

double dec(int l,int use)
{
    if(l==n)
    {
        if(use==k)return 0;
        return -1e20;//?
    }
    if(use==k)return 0;
    if(rec[l][use]!=-1)return rec[l][use];
    double first=0;
    if(use==0)first=M_PI*node[l].rad*node[l].rad;
    double second=M_PI*2*node[l].rad*node[l].height;
    return rec[l][use]=max(dec(l+1,use),dec(l+1,use+1)+first+second);
}

int main()
{
    int tc,tci=0;
    cin>>tc;
    while(tc--)
    {
        cout<<"Case #"<<++tci<<": ";
        cin>>n>>k;
        int i,j;
        for(i=0;i<n;i++)cin>>node[i].rad>>node[i].height;
        sort(node,node+n);
        for(i=0;i<1005;i++)for(j=0;j<1005;j++)rec[i][j]=-1;
        printf("%.8lf\n",dec(0,0));
    }
    return 0;
}
