#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("C:\\Users\\hp\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\hp\\Desktop\\output.txt","w",stdout);
    int t;
    cin>>t;
    int x=0;

    while(t--)
    {
        x++;
        int n,k;
        string s;
        cin>>s;
        n=s.length();
        int ar[n];
        cin>>k;
        for(int i=0;i<n;i++)
        {
            char c;
            c=s[i];
            if(c=='-')
                ar[i]=1;
            else
                ar[i]=0;
        }
        int ans=0;
       // cout<<n<<" "<<k<<"\n";
        for(int i=0;i+k<n+1;i++)
        {
            if(ar[i]==1)
            {//cout<<i<<"\n";
                for(int j=0;j<k;j++)
                {
                    ar[i+j]=ar[i+j]^1;
                }
                ans++;
            }
            //cout<<i;
        }
        int f=0;
        for(int i=0;i<n;i++)
        {
            if(ar[i]==1)
            {
                f=1;
                break;
            }
        }
        if(f==1)
            cout<<"Case #"<<x<<": IMPOSSIBLE\n";
        else
            cout<<"Case #"<<x<<": "<<ans<<"\n";
    }
}
