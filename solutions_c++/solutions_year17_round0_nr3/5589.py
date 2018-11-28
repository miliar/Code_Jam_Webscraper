#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("C-small-1-attempt0.out","w",stdout);
    int nn;
    cin>>nn;
    for(int t=1;t<=nn;t++)
    {
        int n,k;
        cin>>n>>k;
        int arr[n+1];
        memset(arr,0,sizeof arr);
        int rin;
        for(int i=0;i<k;i++)
        {
            int sz=0,mx=-1,l=0,r=0,fl=0;
            for(int j=1;j<=n;j++)
            {
                if(arr[j]>0)
                {
                    if(r>mx)
                    {
                        mx=r;
                        fl=l;
                    }
                    l=j;
                    r=0;
                }
                else
                    r++;
            }
            if(mx<r)
            {
             //   cout<<i<<" mx "<<r<<" "<<l<<endl;
                mx=max(mx,r);
                fl=l;

            }
            //cout<<mx<<endl;
            if(mx%2==0)
            {
               // cout<<i<<" "<<fl<<" "<<mx/2<<endl;
                if(i==k-1)
                    rin=fl+(mx/2);
                arr[fl+(mx/2)]=i+1;
            }
            else
            {
                if(i==k-1)
                    rin=fl+(mx/2)+1;
                arr[fl+(mx/2)+1]=i+1;
            }
        }
        int a=0,b=0;
        for(int i=rin+1;i<=n;i++)
        {
            if(arr[i]>0)
                break;
            a++;
        }
        for(int i=rin-1;i>=1;i--)
        {
            if(arr[i]>0)
                break;
            b++;
        }
        cout<<"Case #"<<t<<": "<<max(a,b)<<" "<<min(a,b)<<endl;
    }
    return 0;
}
