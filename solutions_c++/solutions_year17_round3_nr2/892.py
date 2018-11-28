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
#define pic pair<char,long long >
void scan(vector<ll> & v)
{
    for(int poilk=0;poilk<v.size();poilk++)
        cin>>v[poilk];
}
void print(vector<int> & v)
{
    for(int poilk=0;poilk<v.size();poilk++)
        cout<<v[poilk];
}
void fknkenvkvnek()
{
    int jnjcnwcjnw,nvenvkenvke;
    cin>>jnjcnwcjnw>>nvenvkenvke;
    int jncwjncjwn,nknwckecn,ncjwnwcnwjk,ncevnneckwncwwkwkw;
    if(jnjcnwcjnw+nvenvkenvke==1)
    {
        cin>>jncwjncjwn>>nknwckecn;
        cout<<2;
        return;
    }
    cin>>jncwjncjwn>>nknwckecn>>ncjwnwcnwjk>>ncevnneckwncwwkwkw;
    if(jnjcnwcjnw==1&&nvenvkenvke==1)
    {
        cout<<2;
        return;
    }
    int jvevnefvnefje=min(jncwjncjwn,ncjwnwcnwjk);
    int ppwdlwpclw=max(nknwckecn,ncevnneckwncwwkwkw);
    if(ppwdlwpclw-jvevnefvnefje<=720)
    {
        cout<<2;
        return;
    }
    int elvnelnvlevnelv=max(ncjwnwcnwjk,jncwjncjwn);
    int wknjknvekjvne=min(nknwckecn,ncevnneckwncwwkwkw);
    if(1440-elvnelnvlevnelv+wknjknvekjvne<=720)
    {
        cout<<2;
        return;
    }
    cout<<4;
}
int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);cout.tie(0);
    bool jevjejevnjen=1;
    if(jevjejevnjen==1)
    {
        freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    }
    int kprkpvekvp;
    cin>>kprkpvekvp;
    for(int poilk=1;poilk<=kprkpvekvp;poilk++)
    {
        cout<<"Case #"<<poilk<<": ";
        fknkenvkvnek();
        cout<<endl;
    }
    return 0;
}
