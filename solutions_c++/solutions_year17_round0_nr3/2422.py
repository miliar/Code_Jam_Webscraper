#include<iostream>
#include<string>
using namespace std;
#define ll long long int
int main()
{
    ll t,i,n,k;
    ll high,low,temp_high,temp_low;
    ll ct_high,ct_low,temp_ct_high,temp_ct_low;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
         cout<<"Case #"<<tc<<": ";
         cin>>n>>k;
         i=1;
         high=n/2;
         low=n-1-high;
         ct_high=1;
         ct_low=0;
         if(high!=low)
            ct_low=1;
         else
            ct_high=2;
         if(k<=i)
            {
                cout<<high<<" "<<low<<endl;
                continue;
            }   
         while(1)
         {
             if(high==low)
             {
                i+=ct_high+ct_low;
                temp_high=high/2;
                temp_low=high-1-temp_high;
                if(k<=i)
                {
                    cout<<temp_high<<" "<<temp_low<<endl;
                    break;
                }
                temp_ct_high=(temp_high==temp_low)?2*ct_high:ct_high;
                temp_ct_low=(temp_high==temp_low)?0:ct_high;
             }
             else if(high%2==0)
             {
                i+=ct_high;
                temp_high=high/2;
                temp_low=temp_high-1;
                if(k<=i)
                {
                    cout<<temp_high<<" "<<temp_low<<endl;
                    break;
                }
                i+=ct_low;
                if(k<=i)
                {
                    cout<<temp_low<<" "<<temp_low<<endl;
                    break;
                }
                temp_ct_high=ct_high;
                temp_ct_low=ct_high+2*ct_low;
             }
             else
             {
                i+=ct_high;
                temp_high=high/2;
                temp_low=temp_high-1;
                if(k<=i)
                {
                    cout<<temp_high<<" "<<temp_high<<endl;
                    break;
                }
                i+=ct_low;
                if(k<=i)
                {
                    cout<<temp_high<<" "<<temp_low<<endl;
                    break;
                }
                temp_ct_high=2*ct_high+ct_low;
                temp_ct_low=ct_low;
             }
             high=temp_high,low=temp_low;
             ct_high=temp_ct_high,ct_low=temp_ct_low;
         }
    }
}