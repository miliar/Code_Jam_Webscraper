#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fast ios_base::sync_with_stdio(false); cin.tie(NULL)
int main()
{
    fast;
    ll t,n,i,j, ojha=0;
    cin>>t;
    while(t--)
    {
        ojha++;
        ll k=0;
        ll arr[1000];
        stack<ll>s;
        cin>>n;
        while(n)
        {
            s.push(n%10);
            n/=10;
        }
        while(!s.empty())
        {
            arr[k]=s.top();
            s.pop();
            k++;
        }
        ll idx=0;
        while(true)
        {
            bool change=false;
            if(arr[0]==0)
            {   
                idx=1;
                break;
            }
            for(i=1;i<k;i++)
            {
                if(arr[i]<arr[i-1])
                {
                    change=true;
                    for(j=i;j<k;j++)
                        arr[j]=9;
                    arr[i-1]--;
                    break;
                }
            }
            if(!change)break;
        }
        cout<<"Case #"<<ojha<<": ";
        for(i=idx;i<k;i++)
           cout<<arr[i];
        cout<<"\n";
    }
}