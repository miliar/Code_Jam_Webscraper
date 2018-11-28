#include<bits/stdc++.h>
using namespace std;
long long int ans;
bool tidy(int a[],int n)
{
    for(int i=0;i<n-1;i++)
        if(a[i+1]>a[i])return false;
    return true;
}
bool lesser(int a[],long long int k,long long int m)
{
    long long int num=0;
    for(int i=k-1;i>=0;i--)num=num*10+a[i];
    //cout<<num<<" "<<m;
    ans=num;
    if(num<=m)return true;
    return false;
}
int main()
{
    int t;cin>>t;
    for(int i=1;i<=t;i++)
    {
        long long int n;cin>>n;
        long long int m=n,k;
        int a[20];
        if(n<10){cout<<"Case #"<<i<<": "<<n<<endl;}
        else{
        for(k=0;k<20;k++)
        {
            if(n>0)
            {a[k]=n%10;n=n/10;}
            else break;
        }
        int j=0;
        while(!tidy(a,k) || !lesser(a,k,m))
        {
            if(j==k)break;
            if(a[j]==0)a[j++]=9;
            else a[j]--;
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
        }
    }
}
