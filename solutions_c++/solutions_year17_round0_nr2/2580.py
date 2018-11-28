#include<bits/stdc++.h>
using namespace std;
long long int arr[20];
long long int l;
void conv(string str)
{
    for(long long int i=0;i<str.length();i++)
    {
        arr[i]=str[i]-'0';

    }
}
long long int check[20];
long long int ans()
{
   /* for(long long int i=0;i<l;i++)
        cout<<arr[i]<<' ';
    cout<<endl;*/
    if(l>1)
    {
        if(arr[l-1]<arr[l-2])
        {
            check[l-1]=9;
            check[l-2]=arr[l-2]-1;
        }
        else
        {
            check[l-1]=arr[l-1];
            check[l-2]=arr[l-2];
        }
        for(long long int k=l-3;k>=0;k--)
        {
         //   cout<<arr[k]<<' '<<check[k+1]<<endl;
            if(arr[k]>check[k+1])
            {
                check[k]=arr[k]-1;
                for(long long int s = k+1;s<l;s++)
                    check[s]=9;
            }
            else
            {
                check[k]=arr[k];
            }
        }
    }
    else check[0]=arr[0];
    long long int ans = 0;
    for(long long int i=0;i<l;i++)
    {
        ans=ans*10+check[i];
    }
    return ans;
}
int main()
{
    long long int t;
    cin>>t;
    string str;
    for(int i=1;i<=t;i++)
    {
        cin>>str;
        l=str.length();
        memset(arr,0,sizeof(arr));
        memset(check,0,sizeof(check));
        conv(str);
        cout<<"Case #"<<i<<":"<<' '<<ans()<<endl;

    }
}
