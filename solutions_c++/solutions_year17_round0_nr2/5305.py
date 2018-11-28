#include <bits/stdc++.h>
using namespace std;
long long func5(int* arr,int n)
{
    int flag=0;
    for(int i=1;i<=n-1;i++)
    {
        if(arr[i]>arr[i-1])
        {
            arr[i]=arr[i]-1;
            arr[i-1]=9;
            flag=1;
        }
    }
    long long xx=0;
    for(int i=n-1;i>=0;i--)
        if(arr[i]!=0 || i!=n-1)
        {
            xx=xx*10+arr[i];
        }
    return xx;
}
long long func4(long long a)
{
    //if(a%10==0)a-=1;
    //cout<<a<<endl;
    int d=0,n=0,k=0;
    int arr[18]={0};
    while(a!=0)
    {
        n++;
        d=a%10;
        arr[k++]=d;
        a=a/10;
    }
     return func5(arr,n);
}
int func3(long long a)
{
    int prev=-1,cc=1,d,c=0;
    while(a!=0)
    {
        c++;
        d=a%10;
        if(d<=prev)
            cc++;
        a=a/10;
        prev=d;
    }
    if(cc==c)
        return 1;
    else return 0;
}
//struct x
//{
//    int* arr;
//    int cnt;
//};
long long func2(int* arr,int n)
{
    int flag=0;
    for(int i=n-1;i>=1;i--)
    {
        if(flag==1)
            arr[i-1]=9;
        else if(arr[i]>arr[i-1])
        {
            arr[i]=arr[i]-1;
            arr[i-1]=9;
            flag=1;
        }
    }
    long long xx=0;
    for(int i=n-1;i>=0;i--)
        if(arr[i]!=0 || i!=n-1)
        {
            xx=xx*10+arr[i];
        }
    return xx;
}
long long func(long long a)
{
    //if(a%10==0)a-=1;
    //cout<<a<<endl;
    int d=0,n=0,k=0;
    int arr[18]={0};
    while(a!=0)
    {
        n++;
        d=a%10;
        arr[k++]=d;
        a=a/10;
    }
     return func2(arr,n);
}
int main()
{
    freopen("inputl.in","r",stdin);
    freopen("large.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        long long a;
        cin>>a;
        cout<<"Case #"<<i<<": ";
        long long xx=func(a);
            if(func3(xx)==0)
                xx=func4(xx);
        cout<<xx<<endl;
    }

}
