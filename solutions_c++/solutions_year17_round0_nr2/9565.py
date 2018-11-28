#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    ll tc,n,i,x,count,temp,first,ans;
    cin>>tc;
    for(i=1;i<=tc;i++)
    {
        cin>>n;
        temp=n;
        ans=temp%10;
        temp/=10;
        first=ans;
        count=1;
        while(temp!=0)
        {
           x=temp%10;
           if(x > first)
           {
                x--;
                ans=x*pow((double)10,(double)count)+pow((double)10,(double)count)-1;
             
                first=ans/(pow((double)10,(double)count));
                   count++; 
           // cout<<x<<" "<<temp<<"\n";                                    
           } 
           else
           {
                ans=x*pow((double)10,(double)count)+ans;
                first=ans/(pow((double)10,(double)count));
                count++;
           }
           temp/=10;
            //cout<<temp<<" "<<ans<<"\n";
        }
        cout<<"Case #"<<i<<": "<<ans<<"\n";
    }
    return 0;
}
