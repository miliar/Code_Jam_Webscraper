#include "bits/stdc++.h"
using namespace std;
typedef unsigned long long ull;
typedef long long int ll;
typedef vector<long long int> vi;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
    ll t;
    cin>>t;
    int z=1;
    while(t--)
    {
        ll n,sum=0,count=0,m,flag=0,ans=0,k,t;
        int a[1009]={0};
        count=0;
        string v;
        int b;
        cin>>v>>k;
        n=v.length();
        for(int i=0;i<=n-k;i++)
        {
            if(v[i]=='-')
            {
                if(a[i]%2==0)
                {
                    count++;
                    for(int j=i;j<i+k;j++)
                        a[j]+=1;
                }
            }
            else
            {
                if(a[i]%2!=0)
                {
                    count++;
                    for(int j=i;j<i+k;j++)
                        a[j]+=1;
                }
            }
        }
        for(int i=0;i<n;i++)
        {
            if(v[i]=='-'&&a[i]%2==0)
                ans=-1;
            else if(v[i]=='+'&&a[i]%2==1)
                ans=-1;

        }
        cout<<endl;
        cout<<"Case #"<<z<<": ";
        if(ans==-1)
        {
            cout<<"IMPOSSIBLE";
        }
        else cout<<count;
        cout<<endl;
        z++;
    }
    return 0;
}


/* freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
 */
