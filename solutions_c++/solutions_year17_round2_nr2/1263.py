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
void fun()
{
    int n;
    cin>>n;
    vector<int> v(6);
    scan(v);
    //cout<<"111"<<endl;
    vector<pic> vv(3);
    vv[0]={v[0],'R'};
    vv[1]={v[2],'Y'};
    vv[2]={v[4],'B'};
    //cout<<"122"<<endl;
    sort(vv.begin(),vv.end(),greater<pic>());
    if(vv[0].f>vv[1].f+vv[2].f)
    {
        cout<<"IMPOSSIBLE";
        return;
    }
    list<char> ls;
    for(int i=0;i<vv[0].f;i++)
        ls.push_back(vv[0].s);
    int i=0;
    list<char> ::iterator it;
    for(it=ls.begin(); ;it++)
    {
        if(i==vv[1].f)
            break;
        ls.insert(it,vv[1].s);
        i++;
    }
    i=0;
    if(it==ls.end())
        it=ls.begin();
    for(;;)
    {
        if(i==vv[2].f)
            break;
        ls.insert(it,vv[2].s);
        i++;
        it++;
        if(it==ls.end())
            it=ls.begin();
    }
    list<char> ::iterator it1=ls.begin();
    for(;it1!=ls.end();it1++)
        cout<<*it1;
 }
int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);cout.tie(0);
    bool test=1;
    if(test==1)
    {
        freopen("input_file_name.txt","r",stdin);
        freopen("output_file_name.txt","w",stdout);
    }
    int t=1;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        fun();
        cout<<endl;
    }
    int acc;cin>>acc;
    return 0;
}
