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


void inputttt(vector<int> & v)
{
    for(int i=0;i<v.size();i++)
        cin>>v[i];
}
void preprocess()
{
    int n;
    cin>>n;
    vector<int> v(6);
    inputttt(v);
    vector<pic> vv(3);
    vv[0]={v[0],'R'};
    vv[1]={v[2],'Y'};
    vv[2]={v[4],'B'};
    sort(vv.begin(),vv.end(),greater<pic>());
    if(vv[0].f > vv[1].f+vv[2].f)
    {
        cout<<"IMPOSSIBLE";
        return;
    }
    list<char> listing;
    for(int i=0;i<vv[0].f;i++)
        listing.push_back(vv[0].s);
    int i=0;
    list<char> ::iterator it;
    for(it=listing.begin(); ;it++)
    {
        if(i==vv[1].f)
            break;
        listing.insert(it,vv[1].s);
        i++;
    }
    i=0;
    if(it==listing.end())
        it=listing.begin();
    for(;;)
    {
        if(i==vv[2].f)
            break;
        listing.insert(it,vv[2].s);
        i++;
        it++;
        if(it==listing.end())
            it=listing.begin();
    }
    list<char> ::iterator it1=listing.begin();
    for(;it1!=listing.end();it1++)
        cout<<*it1;
 }
int main()
{
    freopen("E:\\input.txt", "r", stdin);
    freopen("E:\\output.txt", "w", stdout);
    int t=1;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        preprocess();
        cout<<endl;
    }
    return 0;
}
