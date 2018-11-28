#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        int n,p,arr[109];
        cin>>n>>p;
        for(int f=0;f<n;f++)
            cin>>arr[f];
        int ans=0;
        for(int f=0;f<n;f++)
        {
            if(arr[f]%p==0)
            {
                arr[f]=-1;
                ans++;
            }
        }
        if(p>2)
        for(int f=0;f<n;f++)
        {
            if(arr[f]!=-1)
            {
                for(int f1=f+1;f1<n;f1++)
                {
                    if(arr[f1]!=-1&&(arr[f]+arr[f1])%p==0)
                    {
                        arr[f1]=arr[f]=-1;
                        ans++;
                        break;
                    }
                }
            }
        }
        if(p>3)
        for(int f=0;f<n;f++)
        {
            for(int f1=f+1;f1<n&&arr[f]!=-1;f1++)
            {
                for(int f2=f1+1;f2<n&&arr[f1]!=-1;f2++)
                {
                    if(arr[f2]!=-1&&(arr[f]+arr[f1]+arr[f2])%p==0)
                    {
                        arr[f2]=arr[f1]=arr[f]=-1;
                        ans++;
                        break;
                    }
                }
            }
        }
        int fours=0;
        for(int f=0;f<n;f++)
        {
            if(arr[f]!=-1)
                fours++;
        }
        ans+=(fours+p-1)/p;
        cout<<"Case #"<<tc<<": "<<ans<<endl;
    }
}
