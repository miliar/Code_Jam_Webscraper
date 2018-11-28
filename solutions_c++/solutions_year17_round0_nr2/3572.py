#include<bits/stdc++.h>
using namespace std;
int a[20],t,sz;
long long n;
void conv()
{
    sz=0;
    int n2=n;
    while(n2>0)
    {
        sz++;
        n2/=10;
    }
    n2=n;
    int sz2=sz;
    while(n2>0)
    {
        sz2--;
        a[sz2]=n2%10;
        n2/=10;
    }
}
long long comp(int loc)
{
    long long ans=0;
    if(loc>0&&a[loc]<a[loc-1]) return -1;
    if(loc==(sz-1))
        return a[loc];
    ans=comp(loc+1);
    if(ans==-1)
    {
        if(loc!=0&&a[loc]==a[loc-1]) return -1;
        ans=a[loc]-1;
        for(int i=loc+1;i<sz;i++)
        {
            ans=ans*10ll+9;
        }
        return ans;
    }
    long long mult=1;
    for(int i=loc+1;i<sz;i++)
    {
        mult*=10ll;
    }
    ans+=mult*a[loc];
    return ans;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        cin>>n;
        conv();
        cout<<"Case #"<<tc<<": "<<comp(0)<<endl;
    }
}