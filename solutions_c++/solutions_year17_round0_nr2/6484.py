#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    assert(freopen("input.txt","r",stdin));
  assert(freopen("output.txt","w",stdout));
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        ll num;
        cin>>num;
        int n=0;
        ll temp=num;
        while(temp)
        {
            n++;
            temp/=10;
        }
        int arr[n];
        temp=num;
        for(int i=n-1;i>=0;i--)
        {
            arr[i]=num%10;
            num/=10;
        }
        for(int i=n-1;i>=0;i--)
        {
            bool valid=true;
            for(int j=i;j<n;j++)
            {
                if(arr[j]<arr[i])
                {
                    valid=false;
                    break;
                }
            }
            if(!valid)
            {
                arr[i]--;
                for(int j=i+1;j<n;j++)
                    arr[j]=9;
            }
        }
        ll ans=arr[0];
        for(int i=1;i<n;i++)
        {
            ans=ans*10+arr[i];
        }
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
    return 0;
}

