#include<iostream>
#include<stdio.h>
using namespace std;
struct a{
int ls;
int rs;
};
int minn(int x,int y)
{
    if(x<y)
        return x;
    else if(x>y)
        return y;
    else
        return x;
}
int maxx(int x,int y)
{
    if(x>y)
        return x;
    else if(x<y)
        return y;
    else
        return x;
}
int main()
{
    freopen("C-small-1-attempt2.in","r",stdin);
    freopen("C-small-1-attempt2.out","w",stdout);
    int t,i,N,K,ls,rs,j,k,n,ans1,ans2,maxi,z;
    cin>>t;
    for(int c=1;c<=t;c++)
    {

        cin>>N>>K;
        int arr[N+2],temp[N+2];
        struct a var[N+2];
        arr[0]=arr[N+1]=1;
        for(i=1;i<=N;i++)
        {
            arr[i]=0;
        }
        for(n=1;n<=K;n++)
        {

        for(i=1;i<=N;i++)
        {
            var[i].ls=var[i].rs=0;
            j=i-1;
            while(arr[j]!=1)
            {
                (var[i].ls)++;
                j--;
            }
            k=i+1;
            while(arr[k]!=1)
            {
                (var[i].rs)++;
                k++;
            }
            temp[i]=minn((var[i].ls),(var[i].rs));
        }
        /*for(i=1;i<=N;i++)
        {
            cout<<var[i].ls<<" ";
            cout<<var[i].rs<<" ";
            cout<<temp[i]<<endl;
        }*/
        for(i=1;i<=N;i++)
        {
            if(arr[i]==0)
            {
         maxi=temp[1];
         z=i;
         break;
            }
        }
       // cout<<arr[2];
        for(i=2;i<=N;i++)
        {
        if(arr[i]==0)
        {
            if(temp[i]>maxi)
            {
                z=i;
                maxi=temp[i];
            }
            else if(temp[i]==maxi)
            {
                int x,y;
                x=maxx(var[i].ls,var[i].rs);
                y=maxx(var[z].ls,var[z].rs);
              //  cout<<"x="<<x<<"y="<<y;
                if(x>y)
                {
                    z=i;
                }
                else if(x==y)
                {
                    z=minn(i,z);
                }
            }
        }
        }
        arr[z]=1;
        ans1=maxx(var[z].ls,var[z].rs);
        ans2=minn(var[z].ls,var[z].rs);
        }
        /*cout<<"arr:\n";
        for(i=0;i<N+2;i++)
        {
            cout<<arr[i]<<" ";
        }*/
        cout<<"Case #"<<c<<": "<<ans1<<" "<<ans2<<endl;
    }
}
