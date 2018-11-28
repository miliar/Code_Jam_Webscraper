#include <bits/stdc++.h>

using namespace std;

int n,c,m,arr[1009],arr1[1009];

int check(int k)
{
    int car=0,ret=0;
    for(int f=0;f<n;f++)
    {
        if(arr[f]-k>car)
            return -1;
        ret+=max(0,arr[f]-k);
        car+=k-arr[f];
    }
    return ret;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        memset(arr,0,sizeof arr);
        memset(arr1,0,sizeof arr1);
        cin>>n>>c>>m;
        int x,p,maxi=0,ans;
        for(int f=0;f<m;f++)
        {
            cin>>p>>x;
            arr[p-1]++;
            arr1[x]++;
            maxi=max(maxi,arr1[x]);
        }
        for(int f=maxi;f<=m;f++)
        {
            ans=check(f);
            if(ans!=-1)
            {
                cout<<"Case #"<<tc<<": "<<f<<" "<<ans<<endl;
                break;
            }
        }
    }
}
