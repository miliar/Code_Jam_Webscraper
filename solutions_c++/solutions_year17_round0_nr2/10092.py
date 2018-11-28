#include<bits/stdc++.h>
using namespace std;
bool chk(int n,int &a)
{
    int f=0,t=10,n1=n;
    while(n)
    {
        if(n%10==0){
        f=1;
        break;
                }
        if(t<n%10)
        {
            f=1;
        }
        t=n%10;
        n/=10;

    }
    if(f==0)
    {
        a=n1;
        return true;

    }
    return false;
}
int main()
{
int t;
cin>>t;
for(int tc=1;tc<=t;tc++)
{
    //unsigned long long int n;
    int n;
    cin>>n;
    int ans;
    for(int  i=n;i>=0;i--)
    {
        if(chk(i,ans)==true)
            break;

    }

    cout<<"Case #"<<tc<<": ";
    cout<<ans;
    cout<<endl;
}
return 0;
}
