#include<bits/stdc++.h>
using namespace std;
int arr[5000];
int l;
int main()
{
    int t;
    cin>>t;
    string str;
    for(int p=1;p<=t;p++)
    {
        cin>>str;
        int k,ans=0;
        cin>>k;
        for(int i=0;i<str.length();i++)
        {
            if(str[i]=='+')
                arr[i]=1;
            else arr[i]=0;
        }
        l=str.length();
        for(int i=0;i<l+1-k;i++)
        {
            if(arr[i]==0)
            {
                for(int j=0;j<k;j++)
                    arr[i+j]=1-arr[i+j];
                ans++;
            }
        }
        int flag = 1;
        for(int i=0;i<l;i++)
        {
            if(arr[i]==0)
                flag = 0;
        }
        if(flag == 0)
            cout<<"Case #"<<p<<":"<<' '<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<p<<":"<<' '<<ans<<endl;
        memset(arr,0,sizeof(arr));
    }
}
