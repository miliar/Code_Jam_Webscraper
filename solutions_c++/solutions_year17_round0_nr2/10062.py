#include<bits/stdc++.h>
#include<stdint.h>
using namespace std;
typedef uint64_t  ll;
bool ifTidy(ll num)
{
    ll temp,prev=INT_MAX;
    temp=num;
    bool ret=true;
    while(ret && temp!=0)
    {
        if(prev>=temp%10)
        {
            prev=temp%10;
            temp/=10;
        }
        else
        {
            ret=false;
        }
    }
    return ret;

}
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("op.out","w",stdout);
    ll t,it,nod,i,nondecr,stIndex,endIndex,mn,j;
    cin>>t;
    vector<int>digits;
    vector<int>tidy;
    ll n,tmp;
    for(it=1;it<=t;it++)
    {
        cin>>n;
        tmp=n;
        /**
        nod=floor(log(n)/log(10))+1;
        vector<int>digits;

        while(tmp!=0)
        {
            digits.push_back(tmp%10);
            tmp/=10;
        }
        reverse(digits.begin(),digits.end());
        */
        while(ifTidy(tmp)==false)
        {
            tmp--;
        }
        cout<<"Case #"<<it<<": ";
        cout<<tmp<<endl;
    }
    return 0;
}

