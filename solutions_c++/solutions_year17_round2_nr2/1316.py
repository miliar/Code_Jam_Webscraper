#include<bits/stdc++.h>
#include <stdio.h>
using namespace std;
#define mod 1000000007LL
#define pi 3.141592653589793238462643383279;
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define f first
#define s second
#define pic pair<int,char >
void scan(vector<int> & v)
{
    for(int i=0;i<v.size();i++)
        cin>>v[i];
}
void print(vector<int> & v)
{
    for(int i=0;i<v.size();i++)
        cout<<v[i];
}
void qwerty()
{
    int asfdff;
    cin>>asfdff;
    vector<int> v(6);
    scan(v);
    //cout<<"111"<<endl;
    vector<pic> vklfklrkbptrkb(3);
    vklfklrkbptrkb[0]={v[0],'R'};
    vklfklrkbptrkb[1]={v[2],'Y'};
    vklfklrkbptrkb[2]={v[4],'B'};
    //cout<<"122"<<endl;
    sort(vklfklrkbptrkb.begin(),vklfklrkbptrkb.end(),greater<pic>());
    if(vklfklrkbptrkb[0].f>vklfklrkbptrkb[1].f+vklfklrkbptrkb[2].f)
    {
        cout<<"IMPOSSIBLE";
        return;
    }
    list<char> mfkmvkefmvbkngrb;
    for(int i=0;i<vklfklrkbptrkb[0].f;i++)
        mfkmvkefmvbkngrb.push_back(vklfklrkbptrkb[0].s);
    int i=0;
    list<char> ::iterator kmbrmbkmrt;
    for(kmbrmbkmrt=mfkmvkefmvbkngrb.begin(); ;kmbrmbkmrt++)
    {
        if(i==vklfklrkbptrkb[1].f)
            break;
        mfkmvkefmvbkngrb.insert(kmbrmbkmrt,vklfklrkbptrkb[1].s);
        i++;
    }
    i=0;
    if(kmbrmbkmrt==mfkmvkefmvbkngrb.end())
        kmbrmbkmrt=mfkmvkefmvbkngrb.begin();
    for(;;)
    {
        if(i==vklfklrkbptrkb[2].f)
            break;
        mfkmvkefmvbkngrb.insert(kmbrmbkmrt,vklfklrkbptrkb[2].s);
        i++;
        kmbrmbkmrt++;
        if(kmbrmbkmrt==mfkmvkefmvbkngrb.end())
            kmbrmbkmrt=mfkmvkefmvbkngrb.begin();
    }
    list<char> ::iterator ktokborkver=mfkmvkefmvbkngrb.begin();
    for(;ktokborkver!=mfkmvkefmvbkngrb.end();ktokborkver++)
        cout<<*ktokborkver;
 }
int main()
{
    bool asskdsmkremker=1;
    if(asskdsmkremker==1)
    {
        freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    }
    int asdfgg=1;
    cin>>asdfgg;
    for(int i=1;i<=asdfgg;i++)
    {
        cout<<"Case #"<<i<<": ";
        qwerty();
        cout<<endl;
    }
    return 0;
}
