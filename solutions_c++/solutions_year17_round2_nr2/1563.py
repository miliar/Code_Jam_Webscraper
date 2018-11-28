#include<bits/stdc++.h>
#include <stdio.h>
using namespace std;
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
void solve()
{
    int n;
    cin>>n;
    vector<int> v(6);
    scan(v);
    //cout<<"111"<<endl;
    vector<pair<int,char > > vectorc(3);
    vectorc[0]={v[0],'R'};
    vectorc[1]={v[2],'Y'};
    vectorc[2]={v[4],'B'};
    //cout<<"122"<<endl;
    sort(vectorc.begin(),vectorc.end(),greater<pic>());
    if(vectorc[0].f>vectorc[1].f+vectorc[2].f)
    {
        cout<<"IMPOSSIBLE";
        return;
    }
    list<char> list1;
    for(int i=0;i<vectorc[0].f;i++)
        list1.push_back(vectorc[0].s);
    int i=0;
    list<char> ::iterator it;
    for(it=list1.begin(); ;it++)
    {
        if(i==vectorc[1].f)
            break;
        list1.insert(it,vectorc[1].s);
        i++;
    }
    i=0;
    if(it==list1.end())
        it=list1.begin();
    for(;;)
    {
        if(i==vectorc[2].f)
            break;
        list1.insert(it,vectorc[2].s);
        i++;
        it++;
        if(it==list1.end())
            it=list1.begin();
    }
    list<char> ::iterator iterator1=list1.begin();
    for(;iterator1!=list1.end();iterator1++)
        cout<<*iterator1;
 }
int main()
{
    bool testing=1;
    if(testing==1)
    {
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    }
    int testcase;
    scanf("%d",&testcase);
    for(int i=1;i<=testcase;i++)
    {
        cout<<"Case #"<<i<<": ";
        solve();
        cout<<endl;
    }
    return 0;
}
