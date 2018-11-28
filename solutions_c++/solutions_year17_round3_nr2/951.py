#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
using namespace std;
int T,N,M;
struct act
{
    bool cine;
    int st,dr;
    bool operator < (act &other)
    {
        return st<other.st;
    }
};
act V[2005];
int tA,tB;
multiset<int> A,B;
int timp(int st,int dr)
{
    if(st>dr)return 1440-st+dr;
    return dr-st;
}
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>N>>M;
        cout<<"Case #"<<t<<": ";A.clear();B.clear();tA=tB=720;
        for(int i=1;i<=N;i++)
        {
            cin>>V[i].st>>V[i].dr;
            V[i].cine=0;
            tB-=timp(V[i].st,V[i].dr);
        }
        for(int i=N+1;i<=N+M;i++)
        {
            cin>>V[i].st>>V[i].dr;
            V[i].cine=1;
            tA-=timp(V[i].st,V[i].dr);
        }
        sort(V+1,V+1+N+M);
        int nr=0,ti=0;N+=M;
        for(int i=1;i<=N;i++)
        {
            if(V[i].cine==V[i%N+1].cine)
            {
                if(V[i].cine)A.insert(timp(V[i].dr,V[i%N+1].st));
                else B.insert(timp(V[i].dr,V[i%N+1].st));
            }
            else
            {
                nr++;
                ti+=timp(V[i].dr,V[i%N+1].st);
            }
        }
        while(1)
        {
            if(A.empty()&&B.empty())break;
            else if(!A.empty()&&B.empty()){if(tA>=*A.begin()&&tA+tB-*A.begin()>=ti)tA-=*A.begin();else break;A.erase(A.begin());}
            else if(!B.empty()&&A.empty()){if(tB>=*B.begin()&&tA+tB-*B.begin()>=ti)tB-=*B.begin();else break;B.erase(B.begin());}
            else
            {
                if(*A.begin()<*B.begin()&&tA>=*A.begin())
                {
                    if(tA+tB-*A.begin()>=ti)tA-=*A.begin();else break;A.erase(A.begin());
                }
                else if(*A.begin()>=*B.begin()&&tB>=*B.begin())
                {
                    if(tA+tB-*B.begin()>=ti)tB-=*B.begin();else break;B.erase(B.begin());
                }
                else break;
            }
        }
        cout<<nr+2*(A.size()+B.size());
        cout<<"\n";
    }
    return 0;
}
